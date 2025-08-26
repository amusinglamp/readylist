import argparse
import pygraphviz as pgv
import datetime
from importlib.metadata import version
from .core import ReadyList
from .example import ExampleList



def main():
    parser = argparse.ArgumentParser(description="Status-based task management that lets you do things when you and they are ready")
    parser.add_argument("-g", "--greet", type=str, help="Greet the specified name")
    parser.add_argument("--version", action="version", version=f"readylist-cli {version('readylist')}")
    parser.add_argument("-s", "--show", help="Show the current statuses")

    args = parser.parse_args()

    readylist = ReadyList("root", "EXPIRE", datetime.datetime.now())
    if args.greet:
        print(readylist.greet(args.greet))

    if args.show:
        print(ReadyList)

if __name__ == "__main__":
    main()
