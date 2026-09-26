import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

df = pd.read_excel("tracker.xlsx",sheet_name="APPLICANTS")
print("Loaded:", df.shape)

# Remove test records
df = df.drop(columns=["Action", "Days to Deadline", "Priority"])
df = df[df["Name"] != "Test Student"]

# Make sure date columns are real dates
df["Enquiry Date"] = pd.to_datetime(df["Enquiry Date"])
df["Next Deadline"] = pd.to_datetime(df["Next Deadline"])

# Recalculate days left from the raw deadline, as of today
today = pd.Timestamp.today().normalize()
df["Days Left"] = (df["Next Deadline"] - today).dt.days

print("Cleaned:", df.shape)

print("\nMissing values per column:")
print(df.isna().sum())

print("\nStatus counts:")
print(df["Status"].value_counts())

print("\nIntake counts:")
print(df["Intake"].value_counts())