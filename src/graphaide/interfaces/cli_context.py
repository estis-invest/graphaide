from dataclasses import dataclass

@dataclass
class CommandContext:
    args: list[str]

    @property
    def is_help(self) -> bool:
        return "--help" in self.args or "-h" in self.args

    @property
    def is_dry_run(self) -> bool:
        return "--dry-run" in self.args

    @property
    def is_interactive(self) -> bool:
        return "--interactive" in self.args or "-i" in self.args

    @property
    def is_verbose(self) -> bool:
        return "--verbose" in self.args or "-v" in self.args





