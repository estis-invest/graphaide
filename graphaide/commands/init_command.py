from pathlib import Path
from graphaide.context.default_context import DefaultContext as CommandContext
from textwrap import dedent

PROJECT_DIRS = {"data": Path("data"), "figures": Path("figures")}


class InitCommand:
    VALID_FLAGS = {"--help", "--dry-run", "--verbose", "--interactive"}

    @classmethod
    def name(cls) -> str:
        return "init"

    @classmethod
    def description(cls) -> str:
        return "Creates storage directories for projects data and figures."

    @classmethod
    def help(cls) -> str:
        return dedent(
            """
        The 'init' command intializes the project structure for saving data.

        graphaide init                          #  Run command and creates directoies 'data' and 'figures'.
        graphaide init --help/ -h               #  Display help and additional information.
        graphaide init --dry-run                #  Runs command without directory creation.
        graphaide init --verbose/ -v            #  Not implemented.
        graphaide init --interactive/ -i        #  Not implemented.

        """
        )

    @classmethod
    def validate(cls, ctx: CommandContext) -> None:
        unknown = ctx.flags - cls.VALID_FLAGS
        if unknown:
            raise ValueError(
                f"Unknown flag(s) for 'graphaide {cls.name()}': {', '.join(sorted(unknown))}"
            )
        return

    def run(self, ctx: CommandContext):
        base_dir = Path.cwd()
        if ctx.is_help:
            print(InitCommand.help())
            return

        if ctx.is_dry_run:
            print("Dry run: the following directories would be created:")
            for dir_path in PROJECT_DIRS.values():
                print(base_dir / dir_path)
            return

        if ctx.is_verbose:
            print("Verbose output not implemented for command.")
            return

        if ctx.is_interactive:
            print("interactive mode not implemented for command")
            return

        try:
            for dir_path in PROJECT_DIRS.values():
                path = base_dir / dir_path
                path.mkdir(parents=True, exist_ok=True)
        except PermissionError as e:
            print(f"Permission denied while creating:\n{e}")
            return

        except OSError as e:
            print(f"Failed to create project directories:\n{e}")
            return

        else:
            print("Project directories where created at:")
            print("\n".join(str(base_dir / p) for p in PROJECT_DIRS.values()))
