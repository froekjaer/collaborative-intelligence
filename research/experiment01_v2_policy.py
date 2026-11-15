"""Offline reference policy: deterministic fixture, NOT security proof or agent evaluation."""
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Grant:
    actor: str
    parent: str | None
    limit: int
    expires_at: int
    actions: frozenset[str]
    revoked: bool = False

@dataclass(frozen=True)
class Request:
    actor: str
    amount: int
    timestamp: int
    action: str = "reserve"
    approval: bool = False

@dataclass
class Policy:
    mission_cap: int
    grants: dict[str, Grant]
    spent: int = 0
    events: list[dict] = field(default_factory=list)

    def decide(self, request: Request, *, require_approval: bool = False) -> bool:
        reasons = []
        if not isinstance(request.amount, int) or isinstance(request.amount, bool) or request.amount < 0:
            reasons.append("invalid_amount")
        if not isinstance(request.timestamp, int) or isinstance(request.timestamp, bool):
            reasons.append("invalid_time")
        if require_approval and not request.approval:
            reasons.append("missing_approval")
        visited = set()
        current = request.actor
        previous = None
        while current is not None:
            if current in visited:
                reasons.append("cycle")
                break
            visited.add(current)
            grant = self.grants.get(current)
            if grant is None:
                reasons.append("missing_grant")
                break
            if grant.revoked:
                reasons.append("revoked")
            if isinstance(request.timestamp, int) and request.timestamp >= grant.expires_at:
                reasons.append("expired")
            if request.action not in grant.actions:
                reasons.append("action_not_granted")
            if isinstance(request.amount, int) and request.amount > grant.limit:
                reasons.append("grant_limit")
            if previous is not None:
                child = self.grants[previous]
                if child.limit > grant.limit or child.expires_at > grant.expires_at or not child.actions.issubset(grant.actions):
                    reasons.append("delegation_widening")
            previous = current
            current = grant.parent
        if isinstance(request.amount, int) and not isinstance(request.amount, bool):
            if self.spent + request.amount > self.mission_cap:
                reasons.append("cumulative_cap")
        allowed = not reasons
        if allowed:
            self.spent += request.amount
        self.events.append({"actor": request.actor, "allowed": allowed,
                            "reasons": sorted(set(reasons)), "spent_after": self.spent,
                            "chain": sorted(visited)})
        return allowed
