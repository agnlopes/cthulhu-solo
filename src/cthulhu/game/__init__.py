import os
from dataclasses import dataclass, field
from typing import Callable, List

from cthulhu.box.enemies import ElderOne, all_elder_ones
from cthulhu.box.episodes import Episode
from cthulhu.box.investigators import Investigator, all_investigators
from cthulhu.exceptions import InvestigatorNotFound, ElderOneNotFound
from cthulhu.seasons import all_episodes
from transitions import Machine, State

mode = os.getenv("CTHULHU_MODE", "tui")
match mode:
    case "cli":
        from cthulhu.game.ui.cli import GameUI
    case "tui":
        from cthulhu.game.ui.tui import GameUI
    case "gui":
        from cthulhu.game.ui.gui import GameUI
    case "www":
        from cthulhu.game.ui.www import GameUI
    case _:
        raise ValueError(f"Invalid mode: {mode}")


@dataclass
class ElderOneTrack:
    size: int = 8
    green: int = 4
    current: int = 1
    _on_eo_advances_effects: List[Callable] = field(default_factory=list)
    _on_eo_summoned_effects: List[Callable] = field(default_factory=list)

    def advances(self, *args, **kwargs):
        self.current += 1
        if self.current == self.size:
            # TODO: end game
            pass

        self._on_eo_advances(*args, **kwargs)

    def _on_eo_advances(self, *args, **kwargs):
        for effect in self._on_eo_advances_effects:
            effect(*args, **kwargs)


@dataclass
class CthulhuGame:
    selected_investigators: List[str]
    investigators: List[Investigator] = field(default_factory=list)
    elder_one_selected: str = "cthulhu"
    elder_one: ElderOne = field(init=False)
    selected_episode: str = "s1e1"
    episode: Episode = field(init=False)
    episode_id: str = field(init=False)
    track: ElderOneTrack = field(init=False)
    fsm: Machine = field(init=False)
    current_investigator: Investigator = field(init=False)

    def __post_init__(self):
        self.setup_fsm()
        self.setup_board()

    def setup_fsm(self):
        machine_states = [
            State(name="init"),
            State(name="setup", on_enter="setup_board"),
            State(name="playing", on_enter="play_game"),
            State(name="end", on_enter="end_game"),
        ]

        machine_transitions = [
            {"trigger": "setup", "source": "init", "dest": "setup"},
            {"trigger": "play", "source": "setup", "dest": "playing"},
            {"trigger": "end", "source": "playing", "dest": "end"},
        ]

        self.fsm = Machine(
            self, states=machine_states, transitions=machine_transitions, initial="init"
        )

    def setup_board(self):
        # episode
        self.episode = all_episodes[self.selected_episode]

        # investigators
        for investigator in self.selected_investigators:
            if investigator not in all_investigators:
                raise InvestigatorNotFound(investigator)
            self.investigators.append(all_investigators[investigator])

        # TODO: set investigators initial room,

        # elder one
        if self.elder_one_selected not in all_elder_ones:
            raise ElderOneNotFound(self.elder_one_selected)
        self.elder_one = all_elder_ones[self.elder_one_selected]

        # TODO: provide a way to select the investigators order, for now it is the order they were selected
        self.current_investigator = self.investigators[0]


@dataclass
class CthulhuGameController:
    game: CthulhuGame
    ui: GameUI = field(init=False)

    def __post_init__(self):
        self.ui = GameUI(self.game)
