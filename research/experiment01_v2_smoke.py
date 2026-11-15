"""Offline contract checks for Experiment 01 v2, NOT an AI efficacy study."""
from dataclasses import dataclass, field
from typing import Optional
import json

@dataclass(frozen=True)
class Action:
    actor: str
    amount: int
    cap: int
    parent: Optional[str] = None
    approval: bool = False

@dataclass
class Ledger:
    mission_cap: int
    actors: dict
    spent: int = 0
    events: list = field(default_factory=list)

    def execute(self, action: Action, global_enforcement: bool) -> bool:
        local_ok = action.actor in self.actors and action.amount >= 0 and action.amount <= action.cap
        # Actor-specific cap and delegation lineage are synthetic, not an external security proof.
        if local_ok:
            local_ok = action.amount <= self.actors[action.actor]['per_action_cap']
        chain_ok = True
        if action.parent is not None:
            chain_ok = (action.parent in self.actors and
                        self.actors[action.actor].get('parent') == action.parent and
                        self.actors[action.actor]['per_action_cap'] <= self.actors[action.parent]['per_action_cap'])
        global_ok = self.spent + action.amount <= self.mission_cap and chain_ok
        allowed = local_ok and (global_ok if global_enforcement else True)
        if allowed:
            self.spent += action.amount
        self.events.append({'actor': action.actor, 'amount': action.amount,
                            'local_ok': local_ok, 'global_ok': global_ok,
                            'allowed': allowed, 'spent_after': self.spent})
        return allowed

def run_fixture(global_enforcement: bool) -> dict:
    ledger = Ledger(100, {'A': {'per_action_cap': 80},
                          'B': {'per_action_cap': 80, 'parent': 'A'}})
    decisions = [ledger.execute(Action('A', 70, 80), global_enforcement),
                 ledger.execute(Action('B', 60, 80, parent='A'), global_enforcement)]
    return {'mode': 'C3_like' if global_enforcement else 'C2_like',
            'decisions': decisions, 'spent': ledger.spent,
            'mission_invariant_held': ledger.spent <= ledger.mission_cap,
            'events': ledger.events}

if __name__ == '__main__':
    print(json.dumps([run_fixture(False), run_fixture(True)], indent=2))
