import argparse
from importlib.metadata import version
from .core import ReadyList

def main():
    parser = argparse.ArgumentParser(description="ReadyList CLI")
    parser.add_argument("--greet", type=str, help="Greet the specified name")
    parser.add_argument("--version", action="version", version=f"readylist-cli {version('readylist-cli')}")
    args = parser.parse_args()

    readylist = ReadyList()
    if args.greet:
        print(readylist.greet(args.greet))

if __name__ == "__main__":
    main()
