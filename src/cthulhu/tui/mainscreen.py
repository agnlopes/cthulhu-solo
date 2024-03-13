from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Static, Header, Footer, Input, Log, TabbedContent, Markdown
from textual.containers import ScrollableContainer

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

BETH_STATS = """\
Sanity:     [bold green][/ bold green]    [bold magenta][/bold magenta]    [green][/green]  [red][[/red][red]][/red] [magenta][/magenta]   [magenta] [/magenta]
Stress:                    Health: [bold red]  [/bold red]  
"""

CTHULHU_STATS = """\
Health:                   Stage:    
"""

ROOM_STATS = """\
Investigators: 3
The Kid [1/5]
Adam [2/5]
Morgan [1/5]

Enemies: 1
Cultist [0/2]

Items: 0
"""

DISCOVERY_CARDS = """\
 card-1
 card-2
 card-3
"""

INVESTIGAGOR_TURN = """\
- [] actions: 3 attack, run, rest, trade, episode actions
- [] draw cthulhu card
- []investigate or fight?
- [ ]resolv turn
"""

class CharactersSummary(Widget):
    BORDER_TITLE="Characters Stats"
    def compose(self) -> ComposeResult:
        with TabbedContent("Beth", "The Kid", "Adam", "Morgan", "Cthulhu"):
            yield Static(BETH_STATS)
            yield Static(BETH_STATS)
            yield Static(BETH_STATS)
            yield Static(BETH_STATS)
            yield Static(CTHULHU_STATS)


class GameLogs(Log):
    BORDER_TITLE="Logs"


class MainPane(Widget):
    BORDER_TITLE="Main"
    def compose(self):
        with ScrollableContainer():
            yield Static(MAP)


class InvestigatorStats(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.border_title = f"{args[0]}'s Turn"

    def compose(self):
        with TabbedContent("Turn", "Stats", "Discovery Cards"):
            with ScrollableContainer():
                yield Static(INVESTIGAGOR_TURN)
            yield Static(BETH_STATS)
            with ScrollableContainer():
                yield Static(DISCOVERY_CARDS)

class RoomStats(Widget):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.border_title = f"Room: {args[0]}"

    def compose(self):
        with ScrollableContainer():
            yield Markdown(ROOM_STATS)


class UserInput(Input):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.border_title = f"Turn: {args[0]}"

class GridLayout(App):
    CSS_PATH = "mainscreen.tcss"

    def compose(self) -> ComposeResult:
        yield Header(id="header")
        yield InvestigatorStats("Beth", id="elderone-stats", classes="box")
        yield CharactersSummary(id="chars", classes="box")
        yield MainPane(id="main", classes="box")
        yield RoomStats(1, id="room", classes="box")
        yield GameLogs(id="logs", classes="box")
        yield UserInput("Beth", id="shell", classes="inputbox")
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Cthulhu"
        self.sub_title = "Death May Die"

    def on_ready(self) -> None:
        log = self.query_one(Log)
        for i in range(20):
            log.write_line(f"{i}: hello world")

if __name__ == "__main__":
    GridLayout().run()
