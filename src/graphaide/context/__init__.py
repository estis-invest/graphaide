from .default_context import DefaultContext
from .data_context import DataContext


CONTEXTS = {"data": DataContext}


def get_context(command: str):
    return CONTEXTS.get(command, DefaultContext)
