"""C3-alloc: synthetic preallocated budget experiment; not distributed consensus or production authorization.

Authority preallocates disjoint budgets once. Delegates can spend only from their
own persistent local account; child allocations consume parent available funds.
No shared per-action central ledger is needed, but issuance MUST be serialized
and allocation records MUST be protected from cloning/rollback.
"""
import sqlite3


class AllocationLedger:
    def __init__(self, path):
        self.db = sqlite3.connect(path, isolation_level=None, timeout=5)
        self.db.execute('PRAGMA busy_timeout=5000')
        self.db.execute('CREATE TABLE IF NOT EXISTS accounts (actor TEXT PRIMARY KEY, parent TEXT, allocated INTEGER NOT NULL CHECK(allocated>=0), spent INTEGER NOT NULL DEFAULT 0 CHECK(spent>=0), delegated INTEGER NOT NULL DEFAULT 0 CHECK(delegated>=0), revoked INTEGER NOT NULL DEFAULT 0)')
        self.db.execute('CREATE TABLE IF NOT EXISTS actions (actor TEXT, request_id TEXT, amount INTEGER NOT NULL, accepted INTEGER NOT NULL, reason TEXT NOT NULL, PRIMARY KEY(actor,request_id))')

    def _tx(self, work):
        self.db.execute('BEGIN IMMEDIATE')
        try:
            result=work()
            self.db.execute('COMMIT')
            return result
        except BaseException:
            if self.db.in_transaction:
                self.db.execute('ROLLBACK')
            raise

    def seed(self, cap):
        if type(cap) is not int or cap < 0:
            raise ValueError('invalid cap')
        def work():
            self.db.execute('INSERT INTO accounts(actor,parent,allocated) VALUES(?,?,?)',('root',None,cap))
        self._tx(work)

    def allocate(self, parent, child, amount):
        if type(amount) is not int or amount < 0 or child == 'root':
            return False, 'invalid_allocation'
        def work():
            row=self.db.execute('SELECT allocated,spent,delegated,revoked FROM accounts WHERE actor=?',(parent,)).fetchone()
            if row is None or row[3]:
                return False,'parent_invalid'
            # A revoked ancestor must not authorize new child allocations.
            seen=set()
            cursor=parent
            while cursor is not None:
                if cursor in seen:
                    return False,'parent_invalid'
                seen.add(cursor)
                link=self.db.execute('SELECT parent,revoked FROM accounts WHERE actor=?',(cursor,)).fetchone()
                if link is None or link[1]:
                    return False,'parent_invalid'
                cursor=link[0]
            if row[0]-row[1]-row[2] < amount:
                return False,'allocation_exceeds_remaining'
            # Parent pointers are immutable and each child is unique.
            self.db.execute('INSERT INTO accounts(actor,parent,allocated) VALUES(?,?,?)',(child,parent,amount))
            self.db.execute('UPDATE accounts SET delegated=delegated+? WHERE actor=?',(amount,parent))
            return True,'allocated'
        return self._tx(work)

    def revoke(self, actor):
        def work():
            self.db.execute('UPDATE accounts SET revoked=1 WHERE actor=?',(actor,))
        self._tx(work)

    def submit(self, actor, request_id, amount):
        if type(amount) is not int or amount < 0:
            return False,'invalid_amount'
        def work():
            old=self.db.execute('SELECT amount,accepted,reason FROM actions WHERE actor=? AND request_id=?',(actor,request_id)).fetchone()
            if old:
                return (bool(old[1]),old[2]) if old[0]==amount else (False,'idempotency_conflict')
            row=self.db.execute('SELECT allocated,spent,delegated FROM accounts WHERE actor=?',(actor,)).fetchone()
            reason='allowed'
            if row is None:
                reason='missing_account'
            elif amount > row[0]-row[1]-row[2]:
                reason='local_cap'
            else:
                seen=set()
                cursor=actor
                while cursor is not None:
                    if cursor in seen:
                        reason='cycle';break
                    seen.add(cursor)
                    link=self.db.execute('SELECT parent,revoked FROM accounts WHERE actor=?',(cursor,)).fetchone()
                    if link is None or link[1]:
                        reason='revoked_or_missing_ancestor';break
                    cursor=link[0]
            accepted=reason=='allowed'
            if accepted:
                self.db.execute('UPDATE accounts SET spent=spent+? WHERE actor=?',(amount,actor))
            self.db.execute('INSERT INTO actions VALUES(?,?,?,?,?)',(actor,request_id,amount,int(accepted),reason))
            return accepted,reason
        return self._tx(work)

    def close(self):
        self.db.close()
