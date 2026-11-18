import sys
from repofacts import __version__


def main() -> None:
    if "--version" in sys.argv or "-v" in sys.argv:
        print(f"repofacts {__version__}")
        return
    print(f"repofacts v{__version__} — placeholder release. Full build coming soon.")


if __name__ == "__main__":
    main()
