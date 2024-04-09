import argparse
import logging

from cthulhu import config
from cthulhu.box.enemies import all_elder_ones
from cthulhu.box.investigators import all_investigators
from cthulhu.game import CthulhuGame, CthulhuGameController
from cthulhu.seasons import all_episodes


def argparser():
    episodes = all_episodes.keys()
    investigators = all_investigators.keys()
    elder_ones = all_elder_ones.keys()

    parser = argparse.ArgumentParser(
        description="Mythos's Cthulhu Death May Die",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-e",
        "--episode",
        dest="episode",
        type=str,
        default="s1e1" if "s1e1" in episodes else None,
        help=f"Episode to be played, valid values are: {', '.join(episodes)}",
    )
    parser.add_argument(
        "-eo",
        "--elder-one",
        dest="elder_one",
        type=str,
        default="cthulhu" if "cthulhu" in elder_ones else None,
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
    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        help="Enable debug logging",
    )

    return parser.parse_args()


def main():
    args = argparser()
    _l = logging.getLogger(__name__)

    if args.verbose:
        _l.setLevel(logging.DEBUG)

    _l.debug(
        "New game, Episode: %s, ElderOne: %s, Investigators: %s",
        args.episode,
        args.elder_one,
        ", ".join(args.investigators),
    )

    game = CthulhuGame(
        selected_investigators=args.investigators,
        selected_episode=args.episode,
        elder_one_selected=args.elder_one,
    )

    import pdb

    pdb.set_trace()

    controller = CthulhuGameController(game)
    controller.ui.run()


if __name__ == "__main__":
    main()
