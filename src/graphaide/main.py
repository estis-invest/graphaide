import sys
from graphaide.commands import COMMANDS as cmd_lib
from graphaide.context import get_context

APP_NAME = "graphaide"

def welcome_message(sep_char:str ="#", row_width:int = 80) -> None:
    print(f"{sep_char}" * row_width)
    print(f"Welcome to {APP_NAME.title()}!")
    print(f"{sep_char}" * row_width)
    print("\n")


def main():
    all_command_names = {cmd.name(): cmd for cmd in cmd_lib}
    if len(sys.argv) < 2 or sys.argv[1] in ["--help", "-h"]:
        welcome_message()
        print(f"Use: {APP_NAME} <commands> [options]")
        print("Available commands:")
        for v in all_command_names.values():
            print(f"{v.name()}        #  {v.description()}")
        return
    cli_command = sys.argv[1]
    cmd = all_command_names.get(cli_command, False)

    if not cmd:
        print(f"Command 'graphaide {cli_command}' is not found")
        print("Please type:\n\n\t'graphaide --help'\n\n to see available commands")
        return


    options = sys.argv[2:]
    ContextClass = get_context(cli_command)
    ctx = ContextClass(options)

    try:
        cmd.validate(ctx)
    except ValueError as e:
        print(f"Error: {e}")
        print(cmd.help())
        return
    else:
        cmd().run(ctx)

if __name__ == "__main__":
    main()
