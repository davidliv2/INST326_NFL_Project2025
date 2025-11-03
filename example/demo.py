import pandas as pd
from src.nfl_system import StatsDataset, Visualizer, Exporter

df = pd.read_csv("examples/sample_stats.csv")
ds = StatsDataset(df)

lb = ds.leaderboard(stat="yards", position="QB", season=2024, top_n=5)
print(lb)

Visualizer.leaderboard_plot(lb, stat="yards", save_path="out/qb_leaderboard.png", show=False)
Exporter.to_csv(lb, "out/qb_leaderboard.csv")
Exporter.to_json(lb, "out/qb_leaderboard.json")
print("Saved outputs in out/")

