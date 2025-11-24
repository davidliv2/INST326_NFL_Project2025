import matplotlib.pyplot as plt
import os
from typing import Optional
from datasets import AbstractDataset

class Visualizer:
    """Polymorphic visualizer for any AbstractDataset subclass."""

    @staticmethod
    def leaderboard_plot(dataset: AbstractDataset, stat: str,
                         save_path: Optional[str] = None, show: bool = True):
        """Plot a leaderboard using polymorphism with AbstractDataset subclasses."""
        if not isinstance(dataset, AbstractDataset):
            raise TypeError("Visualizer expects an AbstractDataset subclass")

        df = dataset.leaderboard(stat)
        if df.empty:
            print("⚠️ leaderboard_plot: no data to plot")
            return

        with plt.style.context("default"):
            fig, ax = plt.subplots(figsize=(9, 5))
            ax.barh(df["player"], df[stat], color="skyblue")
            ax.set_title(f"Top {len(df)} Players by {stat.title()}", fontsize=14)
            ax.set_xlabel(stat.title(), fontsize=12)
            ax.invert_yaxis()
            plt.tight_layout()

            if save_path:
                os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
                plt.savefig(save_path, dpi=150, bbox_inches="tight")
                print(f"✅ Saved plot: {save_path}")

            if show:
                plt.show()
            else:
                plt.close()
