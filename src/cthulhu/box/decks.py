import random
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Card:
    name: str
    description: str


@dataclass
class InsanityCard(Card):
    pass


@dataclass
class MythosCard(Card):
    mythos_symbol: bool = False


@dataclass
class DiscoveryCardItem:
    name: str
    description: str
    cost: str  # TODO: Model discovery card item cost later
    restrictions: str  # TODO: Model discovery card item restrictions later


@dataclass
class DiscoveryCard(Card):
    name: str
    description: str
    left: DiscoveryCardItem
    right: DiscoveryCardItem


@dataclass
class CardsDeck:
    cards: List[Card] = field(default_factory=list)

    def add(self, card: Card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


@dataclass
class InsanityCardsDeck(CardsDeck):
    cards: List[InsanityCard] = field(default_factory=list)


@dataclass
class MythosCardsDeck(CardsDeck):
    cards: List[MythosCard] = field(default_factory=list)


@dataclass
class DiscoveryCardsDeck(CardsDeck):
    cards: List[DiscoveryCard] = field(default_factory=list)
