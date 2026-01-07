from dataclasses import dataclass
from .default_context import DefaultContext


@dataclass
class DataContext(DefaultContext):
    _FLAG_ALIASES = {
        **DefaultContext._FLAG_ALIASES,
        "-t": "--tree",
        "-d": "--source-file",
        "-c": "--drop",
        "-o": "--output-file",
    }

    @property
    def is_tree(self) -> bool:
        return "--tree" in self.flags
