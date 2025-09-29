# PACKS
from pathlib import Path
import os
import pandas as pd
import numpy as np

root = Path("/Users/mcalvomorrison/Projects/sandbox_py")
os.chdir(root)

data = Path("data/ufc")

dfs = {
    "events": pd.read_csv(data / "Events.csv", delimiter = ","),
    "fighter_stats": pd.read_csv(data / "Fighters Stats.csv", delimiter = ","),
    "fighters": pd.read_csv(data / "Fighters.csv", delimiter = ","),
    "fights": pd.read_csv(data / "Fights.csv", delimiter = ","),
    }

events_df = dfs["events"]
fighter_stats_df = dfs["fighter_stats"]
fighters_df = dfs["fighters"]
fights_df = dfs["fights"]

events_df.info()
fighter_stats_df.info()
fighters_df.info()
fights_df.info()

events_df.head(3)
fighter_stats_df.head(3)
fighters_df.head(3)
fights_df.head(3)

print(events_df.columns)
print(fighter_stats_df.columns)
print(fighters_df.columns)
print(fights_df.columns)

# TRANSFORM

fights_full_df = pd.merge(fights_df, events_df, "left", "Event_Id")
