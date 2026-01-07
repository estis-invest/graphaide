from graphaide.context.data_context import DataContext as CommandContext
from pathlib import Path
from textwrap import dedent

DIRECTORY = Path("data")


class DataCommand:
    VALID_FLAGS = {
        "--help", 
        "--dry-run", 
        "--verbose", 
        "--interactive", 
        "--tree"
    }

    @classmethod
    def name(cls) -> str:
        return "data"

    @classmethod
    def description(cls) -> str:
        return "Reads & Writes data and process data"

    @classmethod
    def help(cls) -> str:
        return dedent("""
        The 'data' command reads and write data files, also light processing like droping column(s) and summary statistics.

        graphaide data                          #  Does not nothing.
        graphaide data --help/ -h               #  Display help and additional information. 
        graphaide data --dry-run                #  Runs command without directory creation.
        graphaide data --verbose/ -v            #  Not implemented.
        graphaide data --interactive/ -i        #  Not implemented.
        graphaide data --tree/ -t               # List all available data files in 'data' directory.


        """)

    @classmethod
    def validate(cls, ctx:CommandContext) -> None:
        unknown = ctx.flags - cls.VALID_FLAGS
        if unknown:
            raise ValueError(f"Unknown flag(s) for 'graphaide {cls.name()}': {', '.join(sorted(unknown))}")
        return

    def print_tree(self) -> None:
        data_dir = Path(Path.cwd()) / Path("data")
        indent_width = 4
        for path in sorted(data_dir.rglob("*")):
            depth = (len(path.relative_to(data_dir).parts) -1) * indent_width
            sep_char = "-" if depth <= 0 else "*"
            indent = " " * depth
            if path.is_dir():
                print(f"{indent} # {path.name}")
            else:
                print(f"{indent} {sep_char} {path.name}")

    def run(self, ctx:CommandContext) -> None:
        if ctx.is_help:
            print(DataCommand.help())
            return

        if ctx.is_tree:
            self.print_tree()
            return
        
