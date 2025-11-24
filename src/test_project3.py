import unittest
import pandas as pd
import os
from datasets import StatsDataset, AbstractDataset
from visualizer import Visualizer
from exporter import Exporter

class TestProject3(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame([
            {"player": "A", "yards": 100, "td": 1},
            {"player": "B", "yards": 150, "td": 2},
        ])
        self.dataset = StatsDataset(self.df)

    def test_leaderboard_polymorphism(self):
        # Visualizer works with any AbstractDataset subclass
        lb = self.dataset.leaderboard("yards")
        self.assertEqual(len(lb), 2)
        Visualizer.leaderboard_plot(self.dataset, "yards", show=False)

    def test_exporter_composition(self):
        # StatsDataset has Exporter via composition
        out_csv = "test_out.csv"
        out_json = "test_out.json"

        self.dataset.export_csv(out_csv)
        self.dataset.export_json(out_json)

        self.assertTrue(os.path.exists(out_csv))
        self.assertTrue(os.path.exists(out_json))

        # Clean up
        os.remove(out_csv)
        os.remove(out_json)

    def test_abstract_dataset_enforcement(self):
        # Cannot instantiate abstract base directly
        with self.assertRaises(TypeError):
            class BadDataset(AbstractDataset):
                pass
            BadDataset()

    def test_leaderboard_content(self):
        lb = self.dataset.leaderboard("yards")
        self.assertEqual(lb.iloc[0]["player"], "B")  # highest yards first
        self.assertEqual(lb.iloc[1]["player"], "A")

if __name__ == "__main__":
    unittest.main()
