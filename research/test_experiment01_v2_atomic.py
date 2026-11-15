import os
import sqlite3
import tempfile
import threading
import unittest
from experiment01_v2_atomic import AtomicPolicy, sign_approval

SECRET=b'fixture-secret-not-production'

class AtomicTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.temp.name,'ledger.sqlite')
        self.p=AtomicPolicy.open(self.path,SECRET)
        self.p.setup('m',100,[('A',None,100,100),('B','A',60,80),('C','B',40,70)])

    def tearDown(self):
        self.p.connection.close()
        self.temp.cleanup()

    def call(self, policy, rid, actor='C', amount=30, time=1, signature=True):
        payload={'mission':'m','request_id':rid,'actor':actor,'amount':amount,'timestamp':time}
        approval=sign_approval(SECRET,payload) if signature else 'invalid'
        return policy.submit('m',rid,actor,amount,time,approval)

    def test_valid_three_hop(self):
        self.assertEqual(self.call(self.p,'r1'),(True,'allowed'))

    def test_missing_signature(self):
        self.assertEqual(self.call(self.p,'r1',signature=False),(False,'approval_invalid'))

    def test_signature_bound_to_amount(self):
        payload={'mission':'m','request_id':'r1','actor':'C','amount':10,'timestamp':1}
        self.assertEqual(self.p.submit('m','r1','C',30,1,sign_approval(SECRET,payload)),(False,'approval_invalid'))

    def test_idempotent_replay(self):
        self.assertEqual(self.call(self.p,'r1'),(True,'allowed'))
        self.assertEqual(self.call(self.p,'r1'),(True,'allowed'))
        self.assertEqual(self.p.connection.execute('SELECT spent FROM missions WHERE mission="m"').fetchone()[0],30)

    def test_idempotency_conflict(self):
        self.call(self.p,'r1')
        self.assertEqual(self.call(self.p,'r1',amount=20),(False,'idempotency_conflict'))

    def test_budget(self):
        for i in range(3): self.assertTrue(self.call(self.p,f'r{i}')[0])
        self.assertEqual(self.call(self.p,'r4'),(False,'cumulative_cap'))

    def test_revocation(self):
        self.p.revoke('m','A')
        self.assertEqual(self.call(self.p,'r1'),(False,'grant_invalid'))

    def test_revocation_blocks_intermediate_actor(self):
        self.p.revoke('m','A')
        self.assertEqual(self.call(self.p,'r1',actor='B'),(False,'grant_invalid'))

    def test_expiry(self):
        self.assertEqual(self.call(self.p,'r1',time=70),(False,'grant_invalid'))

    def test_missing_grant(self):
        self.assertEqual(self.call(self.p,'r1',actor='Z'),(False,'missing_grant'))

    def test_restart_persists_spend(self):
        self.call(self.p,'r1')
        self.p.connection.close()
        self.p=AtomicPolicy.open(self.path,SECRET)
        self.assertEqual(self.p.connection.execute('SELECT spent FROM missions WHERE mission="m"').fetchone()[0],30)

    def test_concurrent_budget_atomicity(self):
        results=[]
        def worker(i):
            p=AtomicPolicy.open(self.path,SECRET)
            try: results.append(self.call(p,f'concurrent-{i}',actor='A',amount=60))
            finally: p.connection.close()
        threads=[threading.Thread(target=worker,args=(i,)) for i in range(2)]
        for t in threads:t.start()
        for t in threads:t.join()
        self.assertEqual(sum(1 for allowed,_ in results if allowed),1)
        self.assertEqual(self.p.connection.execute('SELECT spent FROM missions WHERE mission="m"').fetchone()[0],60)

    def test_failed_setup_rolls_back_all_rows(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.p.setup('partial',100,[('A',None,100,100),('A','B',50,50)])
        self.assertEqual(self.p.connection.execute('SELECT COUNT(*) FROM missions WHERE mission=?',('partial',)).fetchone()[0],0)
        self.assertEqual(self.p.connection.execute('SELECT COUNT(*) FROM grants WHERE mission=?',('partial',)).fetchone()[0],0)

if __name__=='__main__':unittest.main()
