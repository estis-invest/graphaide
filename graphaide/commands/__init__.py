import pkgutil
import importlib
import inspect
from . import __path__ as COMMANDS_PATH


COMMANDS = []

for _, name, _ispkg in pkgutil.iter_modules(COMMANDS_PATH):
    try:
        module = importlib.import_module(f".{name}", package=__name__)
    except ModuleNotFoundError as e:
        print(f"Skipping command module with '{name}': {e}")
        continue
    for cls_name, obj in inspect.getmembers(module, inspect.isclass):
        if (
            module.__name__ == obj.__module__
            and callable(getattr(obj, "name", None))
            and callable(getattr(obj, "run", None))
        ):
            COMMANDS.append(obj)
            globals()[cls_name] = obj

__all__ = [cls.__name__ for cls in COMMANDS] + ["COMMANDS"]
