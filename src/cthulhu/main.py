import argparse

from cthulhu.box.enemies import all_elder_ones
from cthulhu.box.investigators import all_investigators
from cthulhu.game import CthulhuGame, CthulhuGameController
from cthulhu.seasons import all_episodes


def argparser():
    episodes = all_episodes.keys()
    investigators = all_investigators.keys()
    elder_ones = all_elder_ones.keys()

    parser = argparse.ArgumentParser(description="Mythos's Cthulhu Death May Die")

    parser.add_argument(
        "-e",
        "--episode",
        dest="episode",
        type=str,
        default="1",
        help=f"Episode to be played, valid values are: {', '.join(episodes)}",
    )
    parser.add_argument(
        "-eo",
        "--elder-one",
        dest="elder_one",
        type=str,
        default="cthulhu",
        help=f"Elder One to be played, valid values are: {', '.join(elder_ones)} ",
    )
    parser.add_argument(
        "-i",
        "--investigator",
        dest="investigators",
        type=str,
        action="append",
        help=f"investigator's name, valid values are: {', '.join(investigators)} ",
    )
    return parser.parse_args()


def main():
    args = argparser()
    game = CthulhuGame(
        selected_investigators=args.investigators,
        selected_episode=args.episode,
        elder_one_selected=args.elder_one,
    )
    controller = CthulhuGameController(game)
    controller.ui.run()


if __name__ == "__main__":
    main()
