import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_excel("tracker.xlsx",sheet_name="APPLICANTS")
print("Loaded:", df.shape)