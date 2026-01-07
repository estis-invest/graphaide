from typing import Protocol, runtime_checkable
from graphaide.context.base_context import CommandContext


@runtime_checkable
class CLICommand(Protocol):
    VALID_FLAGS: set[str]

    @classmethod
    def name(cls) -> str: ...

    @classmethod
    def description(cls) -> str: ...

    @classmethod
    def help(cls) -> str: ...

    @classmethod
    def validate(cls, ctx: CommandContext) -> None: ...

    def run(self, ctx: CommandContext) -> None: ...
