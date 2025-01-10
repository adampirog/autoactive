"""
Stay active all the time!

Script automatically moves mouse from one corner of the screen to the other
and repeats this action in given interval.

This way you can stay active on your communicator all the time! ;)
"""

from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter

from autoactive import main_loop


def parse_args() -> Namespace:
    parser = ArgumentParser(
        description=__doc__,
        formatter_class=RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-s",
        "--sleep-time",
        type=float,
        default=10,
        help="Sleep time between actions (in minutes)",
    )

    return parser.parse_args()


def main(args: Namespace):
    main_loop(args.sleep_time)


def cli():
    main(parse_args())


if __name__ == "__main__":
    cli()
