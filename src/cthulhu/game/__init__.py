from dataclasses import dataclass, field
import os
from typing import List
from transitions import State, Machine

from cthulhu.box.enemies import ElderOne, all_elder_ones
from cthulhu.box.episodes import Episode
from cthulhu.box.investigators import Investigator, all_investigators
from cthulhu.exceptions import InvestigatorNotFound
from cthulhu.seasons import all_episodes

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
    size: int = 10  # TODO: check this on the box
    green: int = 5  # TODO: check this on the box
    current: int = 1

    def elder_one_advances(self):
        self.track_current += 1


@dataclass
class CthulhuGame:
    selected_investigators: List[str]
    investigators: List[Investigator] = field(default_factory=list)
    elder_one_selected: str = "cthulhu"
    elder_one: ElderOne = field(init=False)
    selected_episode: str = "1"
    episode: Episode = field(init=False)
    episode_id: str = field(init=False)
    track: ElderOneTrack = field(init=False)
    fsm: Machine = field(init=False)
    _is_ritual_disrupted: bool = False
    _is_elderone_on_the_board: bool = False
    game_input: str = ""
    current_investigator: Investigator = field(init=False)

    def __post_init__(self):
        self.set_fsm()
        self.setup()

    def set_fsm(self):
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

    @property
    def is_ritual_disrupted(self):
        return self._is_ritual_disrupted

    @is_ritual_disrupted.setter
    def is_ritual_disrupted(self, value: bool):
        self._is_ritual_disrupted = value

    @property
    def is_elderone_on_the_board(self):
        return self._is_elderone_on_the_board

    @is_elderone_on_the_board.setter
    def is_elderone_on_the_board(self, value):
        self._is_elderone_on_the_board = value

    @property
    def has_game_ended(self):
        if len(self.investigators_alive) < 1 or self.game_input == "quit":
            return True
        return False

    @property
    def investigators_alive(self):
        return [i for i in self.investigators if i.is_alive is True]

    def setup_board(self):
        # episode
        print("setting up game... ")
        self.episode = all_episodes[self.selected_episode]

        # investigators
        for investigator in self.selected_investigators:
            if investigator not in all_investigators:
                raise InvestigatorNotFound(investigator)
            self.investigators.append(all_investigators[investigator])

        # elder one
        if self.elder_one_selected not in all_elder_ones:
            # TODO: create an exception for this
            raise ValueError(self.elder_one_selected)
        self.elder_one = all_elder_ones[self.elder_one_selected]

        self.current_investigator = self.investigators[0]


@dataclass
class CthulhuGameController:
    game: CthulhuGame
    verbosity: int = 0
    ui: GameUI = field(init=False)

    def __post_init__(self):
        self.ui = GameUI(self.game)
