import os
import pandas as pd
import matplotlib.pyplot as plt

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

stages = ["Enquiry", "Documents", "Applied", "Offer", "Visa", "Arrived"]
stage_rank = {"Enquiry": 0, "Documents": 1, "Applied": 2,
              "Offer": 3, "Visa": 4, "Arrived": 5}


active = df[df["Status"] != "Withdrawn"].copy()
active["Stage Rank"] = active["Status"].map(stage_rank)
total = len(active)

print("\nFunnel (students who reached each stage):")
for stage in stages:
    reached = (active["Stage Rank"] >= stage_rank[stage]).sum()
    print(f"{stage:<10} {reached:>3}  ({reached / total:.0%})")

# Enquiries per month
monthly = df.groupby(df["Enquiry Date"].dt.to_period("M")).size()
print("\nEnquiries per month:")
print(monthly)

# Most popular courses
print("\nTop 5 courses:")
print(df["Course"].value_counts().head(5))

# Workload by office
print("\nStudents by office:")
print(df["Office"].value_counts())

# Urgent open cases
open_cases = df[~df["Status"].isin(["Arrived", "Withdrawn"])]
overdue = (open_cases["Days Left"] < 0).sum()
due_week = open_cases["Days Left"].between(0, 7).sum()
print(f"\nOverdue: {overdue}   Due within 7 days: {due_week}")