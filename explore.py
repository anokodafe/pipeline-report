#explore.py
#First look at the tracker data before cleaning
import pandas as pd
df = pd.read_excel("tracker.xlsx", sheet_name="APPLICANTS")

print(df.shape)
print(df.head())

#Fidings from this data
#41 rows 16 columns loaded
#STU-001 is a test student and should be removed
#days to Deadline and Priority are frozen from Excel's last save because the formula uses Today()
#Action column isn't needed