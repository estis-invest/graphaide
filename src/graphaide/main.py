import sys
from graphaide.commands import COMMANDS as cmd_lib

APP_NAME = "graphaide"

def main():
    print(f"Welcome to {APP_NAME.title()}!")

    if len(sys.argv) < 2 or "help" == sys.argv[1]:
        print(f"Use: {APP_NAME} <commands> [options]")
        print("Available commands:")
        for cmd in cmd_lib:
            print(f"{cmd.name()}")
    return


if __name__ == "__main__":
    main()
