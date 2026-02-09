# scripts/02_analysis.py
import pandas as pd

df = pd.read_csv("data/processed/expenses_clean.csv")

summary = df.groupby("category")["amount"].sum().reset_index()
print(summary)
