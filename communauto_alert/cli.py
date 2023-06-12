from __future__ import annotations

import argparse

from importlib.metadata import version


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="communauto-alert", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {version('communauto-alert')}",
    )
    parser.add_argument("latitude", help="your latitude", type=float)

    parser.add_argument("longitude", help="your longitude", type=float)

    parser.add_argument(
        "--interval",
        help="interval between checks in seconds",
        default=30,
        metavar="",
        type=int,
    )
    parser.add_argument(
        "--max-distance",
        help="maximum distance of vehicle in meters",
        default=500,
        metavar="",
        type=int,
    )

    parser.add_argument(
        "--no-prius",
        help='ignore vehicles with the model "Prius C"',
        action="store_true",
    )

    parser.add_argument(
        "--province",
        help='the province where the search will be conducted (AL, NS, ON, QC)',
        choices=['AL', 'NS', 'ON', "QC"],
        default='QC',
        metavar="",
        type=str,
    )

    parser.add_argument(
        "--notify",
        help='apprise compatible configuration file (https://github.com/caronc/apprise/wiki/config)',
        default='',
        metavar="",
        type=str,
    )

    return parser.parse_args()
