from datetime import datetime
from typing import TYPE_CHECKING, List, Optional

from cthulhu.box.enemies import ElderOne
from cthulhu.box.episodes import Episode
from cthulhu.box.investigators import Investigator
from textual import on
from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import Reactive, reactive
from textual.widget import Widget
from textual.widgets import (
    Footer,
    Header,
    Input,
    Log,
    Static,
    TabbedContent,
    TabPane,
)

if TYPE_CHECKING:
    from cthulhu.game import CthulhuGame

# TODO: map should be built dinamically in the episode class
MAP = """
              ┌─────9┌────────────6┌─────5┌─────2
              │     ├┤ O F        ├┤     ││     │
              =     ││          L ││     ││     │
              │     │└────────────┘└──┬──┘│     │
┌────11┌────10│     │┌────────────────┴──4│ O2  │┌─────1
│ L F ├┤ B   ├┤     ├┤      F       O    ├┤     ├┤S II │
│     ││     ││     ││                   ││     ││  II │
└─────┘└─────┘│     │└───┬────────────┬──┘│     │└─────┘
              │     │┌───┴─8┌─────7┌──┴──3│     │
              │     ││AAAAA││  L  ││  F  ││     │   ┌───────────12
              │ GY  ├┤AAAAA├┤     ├┤     ├┤     │   │  F         │
              └─────┘└─────┘└─────┘└─────┘└─────┘   │            =
                                                    └─┬────┐     │
                                            ┌────15┌──┴─14 │     │
                                            │ V   ├┤ L F │ │     │
                                            │     ││     │ │     │
                                            └──┬──┘└─────┘ └──┬──┘
                                            ┌──┴──────────────┴─13
                                            │                    │
                                            │ GR       O      L  │
                                            └────────────────────┘
"""


class TurnStats(Widget):
    BORDER_TITLE = "Turn Stats"

    investigators: Reactive[List[Investigator]] = reactive([], always_update=True)

    def __init__(self, investigators: List[Investigator], **kwargs) -> None:
        super().__init__(**kwargs)
        self.investigators = investigators

    def compose(self) -> ComposeResult:
        with TabbedContent():
            for inv in self.investigators:
                with TabPane(inv.name):
                    yield Static(str(inv))


class CharactersSummary(Widget):
    BORDER_TITLE = "Characters Stats"

    characters: Reactive[List[Investigator | ElderOne]] = reactive(
        default=[], always_update=True
    )

    def __init__(self, characters: List[Investigator | ElderOne], **kwargs) -> None:
        super().__init__(**kwargs)
        self.characters = characters

    def compose(self) -> ComposeResult:
        with TabbedContent():
            for char in self.characters:
                with TabPane(char.name):
                    yield Static(str(char))


class MainPane(Widget):
    BORDER_TITLE = "Main"

    episode: Reactive[Optional[Episode]] = reactive(default=None, always_update=True)

    def __init__(self, episode: Episode, **kwargs) -> None:
        super().__init__(**kwargs)
        self.episode = episode

    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            # yield Static(self.episode.map)
            yield Static(MAP)


class RoomStats(Widget):
    BORDER_TITLE = "Room Stats"

    room: Reactive[Optional[int]] = reactive(default=None, always_update=True)

    def __init__(self, room: Optional[int], **kwargs) -> None:
        super().__init__(**kwargs)
        self.room = room

    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield Static(f"Room: {self.room}")


class GameLogs(Log):
    BORDER_TITLE = "Logs"

    def on_ready(self):
        self.write_line("Game started")


class GameUI(App):
    CSS_PATH = "mainscreen.tcss"
    investigators: Reactive[List[Investigator]] = reactive([], always_update=True)
    time: Reactive[datetime] = reactive(datetime.now)

    def __init__(self, game: "CthulhuGame", **kwargs) -> None:
        super().__init__(**kwargs)
        self.game = game

    def compose(self) -> ComposeResult:
        yield Header(id="header")
        # TODO: include elderone
        yield TurnStats(self.game.investigators, id="turn", classes="box")
        yield CharactersSummary(self.game.investigators, id="chars", classes="box")
        yield MainPane(self.game.episode, id="main", classes="box")
        yield RoomStats(
            # TODO: Get this from current_investigator later
            self.game.investigators[0].room_id,
            id="room",
            classes="box",
        )
        yield GameLogs(id="logs", classes="box")
        yield Input(id="shell", classes="inputbox")
        yield Footer()

    @on(Input.Submitted)
    def update_time(self) -> None:
        self.time = datetime.now()

    def on_mount(self) -> None:
        self.update_time()

    @on(Input.Submitted)
    def update_investigator_health(self, event: Input.Submitted) -> None:
        logs = self.query_one(GameLogs)
        logs.write_line(f"input submitted: {event.value}")

        self.game.investigators[0].health = int(event.value)
        self.investigators = self.game.investigators
