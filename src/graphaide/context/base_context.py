from dataclasses import dataclass
from functools import cached_property
from typing import ClassVar

@dataclass
class CommandContext:
    args: list[str]

    _FLAG_ALIASES : ClassVar[dict[str, str]] = None


    @cached_property
    def flags(self) -> set[str]:
        return {
            self.FLAG_ALIASES.get(arg, arg) for arg in self.args if arg.startswith("-")
        }

    @property
    def FLAG_ALIASES(self) -> dict[str, str]:
        return dict(self._FLAG_ALIASES or {})

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
