from dataclasses import dataclass
from .default_context import DefaultContext

@dataclass
class DataContext(DefaultContext):
    _FLAG_ALIASES = {
        **DefaultContext._FLAG_ALIASES,
        "-t": "tree",
        "-s": "--source-file",
        "-c": "--clean",
        "-o": "--output-file"
    }
