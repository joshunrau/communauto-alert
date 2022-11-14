import argparse

from importlib.metadata import version

def main() -> None:
    parser = argparse.ArgumentParser(prog='communauto-alert', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version('communauto-alert')}")
    parser.add_argument('latitude', help='your latitude', type=float)
    parser.add_argument('longitude', help='your longitude', type=float)
    parser.add_argument('--max_distance', help='max distance of vehicle in meters', default=500, metavar='', type=int)
    args = parser.parse_args()
