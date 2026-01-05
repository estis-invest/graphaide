import sys
from graphaide.commands import COMMANDS as cmd_lib
from graphaide.interfaces.cli_context import CommandContext

APP_NAME = "graphaide"

def welcome_message(sep_char:str ="#", row_width:int = 80) -> None:
    print(f"{sep_char}" * row_width)
    print(f"Welcome to {APP_NAME.title()}!")
    print(f"{sep_char}" * row_width)
    print("\n")


def main():
    welcome_message()
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
        print(f"Use: {APP_NAME} <commands> [options]")
        print("Available commands:")
        for cmd in cmd_lib:
            print(f"{cmd.name()}        #  {cmd.description()}")
        return
    cli_command = sys.argv[1]
    options = sys.argv[2:]
    ctx = CommandContext(options)

    for cmd in cmd_lib:
        if cmd.name() == cli_command:
            print(cmd().run(ctx))


if __name__ == "__main__":
    main()
