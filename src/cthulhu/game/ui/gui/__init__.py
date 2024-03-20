from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cthulhu.game import CthulhuGame


class GameUI:
    def __init__(self, game: "CthulhuGame", **kwargs) -> None:
        super().__init__(**kwargs)
        self.game = game

    def run(self):
        print("gui mode not implemented yet.")
