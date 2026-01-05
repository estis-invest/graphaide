from dataclasses import dataclass
from .base_context import CommandContext

@dataclass
class DefaultContext(CommandContext):
    """The default context provider for all commands"""
    pass

