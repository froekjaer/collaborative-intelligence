import unittest
from experiment01_v2_smoke import Action, Ledger, run_fixture

class ContractTests(unittest.TestCase):
    def test_local_only_does_not_account_for_aggregate(self):
        result = run_fixture(False)
        self.assertEqual(result['decisions'], [True, True])
        self.assertFalse(result['mission_invariant_held'])

    def test_global_accounting_blocks_second_action(self):
        result = run_fixture(True)
        self.assertEqual(result['decisions'], [True, False])
        self.assertTrue(result['mission_invariant_held'])
        self.assertEqual(result['spent'], 70)

    def test_valid_boundary_is_allowed(self):
        ledger = Ledger(100, {'A': {'per_action_cap': 100}})
        self.assertTrue(ledger.execute(Action('A', 100, 100), True))

    def test_parent_mismatch_is_rejected(self):
        ledger = Ledger(100, {'A': {'per_action_cap': 80}, 'B': {'per_action_cap': 80, 'parent': 'A'}})
        self.assertFalse(ledger.execute(Action('B', 10, 80, parent='X'), True))

    def test_unauthorised_actor_rejected(self):
        ledger = Ledger(100, {'A': {'per_action_cap': 80}})
        self.assertFalse(ledger.execute(Action('C', 10, 80), True))

    def test_negative_amount_rejected(self):
        ledger = Ledger(100, {'A': {'per_action_cap': 80}})
        self.assertFalse(ledger.execute(Action('A', -1, 80), True))

if __name__ == '__main__':
    unittest.main()
