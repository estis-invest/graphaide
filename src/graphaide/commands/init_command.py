from pathlib import Path
from graphaide.interfaces.cli_context import CommandContext

PROJECT_DIRS = {
    "data": Path("data"),
    "figures": Path("figures")
}

class InitCommand:
    @classmethod
    def name(cls) -> str:
        return "init"

    @classmethod
    def description(cls) -> str:
        return "Creates storage directories for projects data and figures."

    @classmethod
    def help(cls) -> str:
        return """
        The 'init' command intializes the project structure for saving data.

        graphaide init      #  Run command and creates directoies 'data' and 'figures'.
        graphaide init --help/ -h       #  Display help and additional information. 
        graphaide init --dry-run        #  Runs command without directory creation.
        graphaide init --verbose/ -v       #  Not implemented.
        graphaide init --interactive/ -i       #  Not implemented.

        """

    def run(self, ctx:CommandContext):
        if ctx.is_help:
            return InitCommand.help()

        if ctx.is_dry_run:
            return "Command executed without directory creation."
        # base_dir = Path.cwd()
        # for dir_path in PROJECT_DIRS.values():
        #     path = base_dir / dir_path
        #     path.mkdir(parents=True, exist_ok=True)
        # print("\nProject directories where created at:")
        # print("\n".join(str(base_dir / p) for p in PROJECT_DIRS.values()))



