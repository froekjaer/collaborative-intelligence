"""Synthetic offline authorization fixture. NOT production authorization or approval."""
import hashlib
import hmac
import json
import sqlite3
from dataclasses import dataclass


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def sign_approval(secret, payload):
    """Fixture-only shared-secret proof; NOT authenticated human approval."""
    return hmac.new(secret, canonical(payload), hashlib.sha256).hexdigest()


@dataclass
class AtomicPolicy:
    connection: sqlite3.Connection
    secret: bytes

    @classmethod
    def open(cls, path, secret):
        db = sqlite3.connect(path, isolation_level=None, timeout=5)
        db.execute('PRAGMA busy_timeout=5000')
        db.execute('CREATE TABLE IF NOT EXISTS missions (mission TEXT PRIMARY KEY, cap INTEGER NOT NULL CHECK(cap>=0), spent INTEGER NOT NULL DEFAULT 0 CHECK(spent>=0))')
        db.execute('CREATE TABLE IF NOT EXISTS grants (mission TEXT, actor TEXT, parent TEXT, lim INTEGER NOT NULL, expires INTEGER NOT NULL, revoked INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(mission,actor))')
        db.execute('CREATE TABLE IF NOT EXISTS requests (mission TEXT, request_id TEXT, fingerprint TEXT, accepted INTEGER NOT NULL, reason TEXT, PRIMARY KEY(mission,request_id))')
        return cls(db, secret)

    def setup(self, mission, cap, grants):
        if not isinstance(cap, int) or isinstance(cap, bool) or cap < 0:
            raise ValueError('invalid cap')
        db = self.connection
        db.execute('BEGIN IMMEDIATE')
        try:
            db.execute('INSERT INTO missions(mission,cap) VALUES(?,?)', (mission,cap))
            for actor,parent,limit,expiry in grants:
                db.execute('INSERT INTO grants(mission,actor,parent,lim,expires) VALUES(?,?,?,?,?)', (mission,actor,parent,limit,expiry))
            db.execute('COMMIT')
        except BaseException:
            if db.in_transaction:
                db.execute('ROLLBACK')
            raise

    def revoke(self, mission, actor):
        db = self.connection
        db.execute('BEGIN IMMEDIATE')
        try:
            db.execute('UPDATE grants SET revoked=1 WHERE mission=? AND actor=?',(mission,actor))
            db.execute('COMMIT')
        except BaseException:
            if db.in_transaction:
                db.execute('ROLLBACK')
            raise

    def submit(self, mission, request_id, actor, amount, timestamp, approval=None):
        if not isinstance(amount,int) or isinstance(amount,bool) or amount<0 or not isinstance(timestamp,int) or isinstance(timestamp,bool):
            return False,'invalid_input'
        payload={'mission':mission,'request_id':request_id,'actor':actor,'amount':amount,'timestamp':timestamp}
        fingerprint=hashlib.sha256(canonical(payload)).hexdigest()
        db=self.connection
        db.execute('BEGIN IMMEDIATE')
        try:
            previous=db.execute('SELECT fingerprint,accepted,reason FROM requests WHERE mission=? AND request_id=?',(mission,request_id)).fetchone()
            if previous:
                db.execute('COMMIT')
                return (bool(previous[1]),previous[2]) if previous[0]==fingerprint else (False,'idempotency_conflict')
            row=db.execute('SELECT cap,spent FROM missions WHERE mission=?',(mission,)).fetchone()
            reason='allowed'
            if row is None:
                reason='missing_mission'
            elif amount+row[1]>row[0]:
                reason='cumulative_cap'
            else:
                seen=set()
                current=actor
                child=None
                while current is not None:
                    if current in seen:
                        reason='delegation_cycle';break
                    seen.add(current)
                    grant=db.execute('SELECT parent,lim,expires,revoked FROM grants WHERE mission=? AND actor=?',(mission,current)).fetchone()
                    if grant is None:
                        reason='missing_grant';break
                    parent,lim,expires,revoked=grant
                    if revoked or timestamp>=expires or amount>lim:
                        reason='grant_invalid';break
                    if child is not None and (child[1]>lim or child[2]>expires):
                        reason='delegation_widening';break
                    child=grant
                    current=parent
                if reason=='allowed' and (not isinstance(approval,str) or not hmac.compare_digest(approval,sign_approval(self.secret,payload))):
                    reason='approval_invalid'
            accepted=reason=='allowed'
            if accepted:
                db.execute('UPDATE missions SET spent=spent+? WHERE mission=?',(amount,mission))
            db.execute('INSERT INTO requests VALUES(?,?,?,?,?)',(mission,request_id,fingerprint,int(accepted),reason))
            db.execute('COMMIT')
            return accepted,reason
        except BaseException:
            if db.in_transaction:
                db.execute('ROLLBACK')
            raise
