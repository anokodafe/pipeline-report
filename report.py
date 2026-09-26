import pandas as pd
df = pd.read_excel("tracker.xlsx", sheet_name="APPLICANTS")
print(df.shape)
print(df.head())