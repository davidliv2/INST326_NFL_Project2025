from abc import ABC, abstractmethod
import pandas as pd
import os
from typing import Optional
from exporter import Exporter

class AbstractDataset(ABC):
    """Abstract base class for any dataset."""

    @property
    @abstractmethod
    def df(self) -> pd.DataFrame:
        """Return a DataFrame representation of the dataset."""
        pass

    @abstractmethod
    def leaderboard(self, stat: str, **kwargs) -> pd.DataFrame:
        """Return a leaderboard for a stat."""
        pass


class StatsDataset(AbstractDataset):
    """NFL stats dataset with exporter composition."""

    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("StatsDataset requires a DataFrame")
        self._df = df.copy()
        self.exporter = Exporter()  # composition: dataset has an exporter

    @property
    def df(self) -> pd.DataFrame:
        return self._df.copy()

    def leaderboard(self, stat: str, position: Optional[str] = None,
                    season: Optional[int] = None, top_n: int = 10) -> pd.DataFrame:
        data = self._df.copy()
        if "player" not in data.columns or stat not in data.columns:
            print(f"⚠️ leaderboard: missing 'player' or '{stat}' column")
            return pd.DataFrame()

        if season is not None and "season" in data.columns:
            data = data[data["season"] == season]

        if position is not None and "position" in data.columns:
            data = data[data["position"].str.upper() == position.upper()]

        out = (
            data.groupby("player")[stat]
            .sum(numeric_only=True)
            .reset_index()
            .sort_values(stat, ascending=False)
            .head(top_n)
        )
        out.insert(0, "rank", range(1, len(out) + 1))
        return out[["rank", "player", stat]]

    # Export convenience methods using composition
    def export_csv(self, path: str):
        self.exporter.to_csv(self._df, path)

    def export_json(self, path: str):
        self.exporter.to_json(self._df, path)
