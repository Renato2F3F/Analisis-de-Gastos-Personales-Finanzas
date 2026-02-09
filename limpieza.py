# scripts/01_clean_expenses.py
import pandas as pd

df = pd.read_csv("data/raw/expenses_raw.csv")
df["date"] = pd.to_datetime(df["date"])
df.to_csv("data/processed/expenses_clean.csv", index=False)

print("✔ Gastos limpios.")
