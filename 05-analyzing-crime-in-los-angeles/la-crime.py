# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes.head()

# Determine which hour has the highest frequency of crimes
crimes["hour_occ"] = crimes["TIME OCC"].str[:2].astype(int)
sns.countplot(data=crimes, x="hour_occ")
peak_crime_hour = 12

# Determine which area has the highest frequency of night crimes

# Filter df to rows where a crime occurred after 10pm and before 4am
night_crimes = crimes[crimes["hour_occ"].isin([22, 23, 0, 1, 2, 3])]

# Filter for area with the most crime within timeframe of 10pm-4am
peak_night_crime_location = (
    night_crimes
        .groupby("AREA NAME", as_index=False)["hour_occ"]
        .count()
        .sort_values("hour_occ", ascending=False)
        .iloc[0]["AREA NAME"]
)

print(f"The area with the largest volume of night crime is {peak_night_crime_location}")

# Identify the number of crimes committed against victims of different age groups

# Create bins and labels
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Adding new column to the crimes df containing bins for ages and labels
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels)

# Count the crimes by victim age groups
victim_ages = crimes["Age Bracket"].value_counts()
index = victim_ages.index[0]
value = victim_ages.iloc[0]
print(f"The age group with the highest number of victims is the {index} age group, with {value} total crimes against")