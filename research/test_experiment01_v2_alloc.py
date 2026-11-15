"""Deterministic C3-alloc invariants; no live agents or network."""
import os
import sqlite3
import tempfile
import threading
import unittest
from experiment01_v2_alloc import AllocationLedger


class AllocationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.path=os.path.join(self.temp.name,'alloc.sqlite')
        self.p=AllocationLedger(self.path)
        self.p.seed(100)

    def tearDown(self):
        self.p.close()
        self.temp.cleanup()

    def test_allocations_are_disjoint(self):
        self.assertEqual(self.p.allocate('root','a',60),(True,'allocated'))
        self.assertEqual(self.p.allocate('root','b',50),(False,'allocation_exceeds_remaining'))
        self.assertEqual(self.p.allocate('root','b',40),(True,'allocated'))
        self.assertEqual(self.p.submit('a','a1',60),(True,'allowed'))
        self.assertEqual(self.p.submit('b','b1',40),(True,'allowed'))
        self.assertEqual(self.p.submit('root','r1',1),(False,'local_cap'))

    def test_delegation_reserves_parent_budget(self):
        self.p.allocate('root','a',70)
        self.p.allocate('a','c',50)
        self.assertEqual(self.p.submit('a','a1',21),(False,'local_cap'))
        self.assertEqual(self.p.submit('a','a2',20),(True,'allowed'))
        self.assertEqual(self.p.submit('c','c1',50),(True,'allowed'))

    def test_revocation_checks_ancestors(self):
        self.p.allocate('root','a',60)
        self.p.allocate('a','c',30)
        self.p.revoke('a')
        self.assertEqual(self.p.submit('c','c1',10),(False,'revoked_or_missing_ancestor'))

    def test_revoked_ancestor_cannot_issue_new_allocation(self):
        self.p.allocate('root','a',60)
        self.p.revoke('root')
        self.assertEqual(self.p.allocate('a','c',10),(False,'parent_invalid'))

    def test_duplicate_action_does_not_double_spend(self):
        self.p.allocate('root','a',50)
        self.assertEqual(self.p.submit('a','x',30),(True,'allowed'))
        self.assertEqual(self.p.submit('a','x',30),(True,'allowed'))
        self.assertEqual(self.p.submit('a','x',31),(False,'idempotency_conflict'))
        self.assertEqual(self.p.db.execute('SELECT spent FROM accounts WHERE actor="a"').fetchone()[0],30)

    def test_failed_child_creation_does_not_reserve_budget(self):
        self.p.allocate('root','a',40)
        with self.assertRaises(sqlite3.IntegrityError):
            self.p.allocate('root','a',20)
        self.assertEqual(self.p.db.execute('SELECT delegated FROM accounts WHERE actor="root"').fetchone()[0],40)

    def test_restart_preserves_allocation(self):
        self.p.allocate('root','a',40)
        self.p.close()
        self.p=AllocationLedger(self.path)
        self.assertEqual(self.p.submit('a','x',40),(True,'allowed'))
        self.assertEqual(self.p.submit('a','y',1),(False,'local_cap'))

    def test_concurrent_spend_cannot_exceed_local_cap(self):
        self.p.allocate('root','a',60)
        outcomes=[]
        errors=[]
        def run(i):
            ledger=AllocationLedger(self.path)
            try: outcomes.append(ledger.submit('a',str(i),40))
            except Exception as e: errors.append(e)
            finally: ledger.close()
        threads=[threading.Thread(target=run,args=(i,)) for i in range(2)]
        for t in threads: t.start()
        for t in threads: t.join()
        self.assertEqual(errors,[])
        self.assertEqual(sum(1 for allowed,_ in outcomes if allowed),1)
        self.assertEqual(self.p.db.execute('SELECT spent FROM accounts WHERE actor="a"').fetchone()[0],40)

    def test_invalid_amount_and_bool(self):
        self.assertEqual(self.p.allocate('root','a',True),(False,'invalid_allocation'))
        self.assertEqual(self.p.submit('root','x',True),(False,'invalid_amount'))
        self.assertEqual(self.p.submit('root','y',-1),(False,'invalid_amount'))

if __name__=='__main__':
    unittest.main()
