from typing import Protocol, runtime_checkable

@runtime_checkable
class CLICommand(Protocol):
    @classmethod
    def name(cls) -> str: ...
    def run(self, *args: str) -> None: ...
