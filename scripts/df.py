import pandas as pd
import os
import numpy as np

df = pd.read_csv("md_sources.csv")
print("Loaded md_sources.csv with", len(df), "rows.")
print(df.head())