import unittest
from experiment01_v2_policy import Grant, Policy, Request

def grant(actor, parent=None, limit=100, expires=100, actions=frozenset({'reserve'}), revoked=False):
    return Grant(actor, parent, limit, expires, actions, revoked)

class PolicyContractTests(unittest.TestCase):
    def test_authorised_boundary(self):
        p = Policy(100, {'A': grant('A')})
        self.assertTrue(p.decide(Request('A', 100, 99)))
        self.assertEqual(p.spent, 100)

    def test_cumulative_cap(self):
        p = Policy(100, {'A': grant('A')})
        self.assertTrue(p.decide(Request('A', 70, 1)))
        self.assertFalse(p.decide(Request('A', 40, 2)))
        self.assertIn('cumulative_cap', p.events[-1]['reasons'])

    def test_expiry_boundary(self):
        p = Policy(100, {'A': grant('A')})
        self.assertFalse(p.decide(Request('A', 1, 100)))

    def test_revocation_inherited(self):
        p = Policy(100, {'A': grant('A', revoked=True), 'B': grant('B', 'A', 50)})
        self.assertFalse(p.decide(Request('B', 1, 1)))
        self.assertIn('revoked', p.events[-1]['reasons'])

    def test_narrow_chain(self):
        p = Policy(100, {'A': grant('A'), 'B': grant('B', 'A', 70), 'C': grant('C', 'B', 40)})
        self.assertTrue(p.decide(Request('C', 30, 1)))

    def test_widening_chain_rejected(self):
        p = Policy(100, {'A': grant('A', limit=50), 'B': grant('B', 'A', 70)})
        self.assertFalse(p.decide(Request('B', 40, 1)))
        self.assertIn('delegation_widening', p.events[-1]['reasons'])

    def test_cycle(self):
        p = Policy(100, {'A': grant('A', 'B'), 'B': grant('B', 'A')})
        self.assertFalse(p.decide(Request('A', 1, 1)))

    def test_missing_parent(self):
        p = Policy(100, {'B': grant('B', 'A')})
        self.assertFalse(p.decide(Request('B', 1, 1)))

    def test_approval(self):
        p = Policy(100, {'A': grant('A')})
        self.assertFalse(p.decide(Request('A', 1, 1), require_approval=True))
        self.assertTrue(p.decide(Request('A', 1, 1, approval=True), require_approval=True))

    def test_action_scope(self):
        p = Policy(100, {'A': grant('A')})
        self.assertFalse(p.decide(Request('A', 1, 1, action='release_data')))

    def test_false_refusal_guard(self):
        p = Policy(100, {'A': grant('A', limit=50)})
        self.assertTrue(p.decide(Request('A', 50, 1)))

    def test_rejected_action_does_not_spend(self):
        p = Policy(100, {'A': grant('A', limit=20)})
        self.assertFalse(p.decide(Request('A', 21, 1)))
        self.assertEqual(p.spent, 0)

    def test_child_expiry_cannot_exceed_parent(self):
        p = Policy(100, {'A': grant('A', expires=40), 'B': grant('B', 'A', expires=50)})
        self.assertFalse(p.decide(Request('B', 1, 1)))

    def test_child_action_cannot_exceed_parent(self):
        p = Policy(100, {'A': grant('A'), 'B': grant('B', 'A', actions=frozenset({'reserve', 'release_data'}))})
        self.assertFalse(p.decide(Request('B', 1, 1)))

    def test_invalid_negative(self):
        p = Policy(100, {'A': grant('A')})
        self.assertFalse(p.decide(Request('A', -1, 1)))

    def test_invalid_boolean_amount(self):
        p = Policy(100, {'A': grant('A')})
        self.assertFalse(p.decide(Request('A', True, 1)))

if __name__ == '__main__':
    unittest.main()
