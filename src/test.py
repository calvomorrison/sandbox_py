# PACKS
import pandas as pd
import numpy as np

# DATA 
events_df = pd.read_csv("data/ufc/Events.csv", delimiter= ",")
fighter_stats_df = pd.read_csv("data/ufc/Fighters Stats.csv", delimiter=",")
fighters_df = pd.read_csv("data/ufc/Fighters.csv", delimiter=",")
fights_df = pd.read_csv("data/ufc/Fights.csv", delimiter=",")

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