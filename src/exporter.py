"""
Simple exporting utility class used via composition by StatsDataset.
"""

import pandas as pd

class Exporter:
    """Handles exporting DataFrames to CSV and JSON."""

    def to_csv(self, df: pd.DataFrame, filepath: str):
        df.to_csv(filepath, index=False)
        return filepath

    def to_json(self, df: pd.DataFrame, filepath: str):
        df.to_json(filepath, orient="records")
        return filepath
