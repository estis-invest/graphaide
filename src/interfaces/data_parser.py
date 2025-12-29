from typing import Protocol, runtime_checkable
from pathlib import Path
import pandas as pd

@runtime_checkable
class DataParser(Protocol):
    def read_data_source(self) -> Path:
        """Return a path to the data source path.
        """
        ...

    def process_data(self, source: Path) -> pd.DataFrame:
        """
        Loads and process data as a DataFrame. 
        """
        ...

