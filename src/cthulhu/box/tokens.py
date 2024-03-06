from typing import List, Callable
from dataclasses import dataclass, field


@dataclass
class Token:
    token_type: str
    effects: List[Callable] = field(default_factory=list)


@dataclass
class FireToken(Token):
    token_type: str = "fire"
    stinguishable: bool = False


@dataclass
class GateToken(Token):
    token_type: str = "gate"
    color: str = ""


@dataclass
class PlayerStartToken(Token):
    token_type: str = "player_start"
