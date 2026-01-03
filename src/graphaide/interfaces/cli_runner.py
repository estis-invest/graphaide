from typing import Protocol, runtime_checkable
from graphaide.interfaces.cli_context import CommandContext

@runtime_checkable
class CLICommand(Protocol):
    @classmethod
    def name(cls) -> str: ...

    @classmethod
    def description(cls) -> str: ...

    @classmethod
    def help(self) -> str: ...

    def run(self, ctx: CommandContext) -> None: ...

