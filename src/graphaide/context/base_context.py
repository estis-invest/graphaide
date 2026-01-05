from dataclasses import dataclass
from functools import cached_property

@dataclass
class CommandContext:
    args: list[str]

    FLAG_ALIASES = {
        "-h": "--help",
        "-v": "--verbose",
        "-i": "--interactive"
    }

    @cached_property
    def flags(self) -> set[str]:
        return {
            self.FLAG_ALIASES.get(arg, arg) for arg in self.args if arg.startswith("-")

        }

    @property
    def is_help(self) -> bool:
        return "--help" in self.flags

    @property
    def is_dry_run(self) -> bool:
        return "--dry-run" in self.flags

    @property
    def is_interactive(self) -> bool:
        return "--interactive" in self.flags

    @property
    def is_verbose(self) -> bool:
        return "--verbose" in self.flags
