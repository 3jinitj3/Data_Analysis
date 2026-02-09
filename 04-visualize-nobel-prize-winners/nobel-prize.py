# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Import csv and transform to dataframe using pandas
nobel_df = pd.read_csv("data/nobel.csv")

# Look at df columns and datatypes
print(nobel_df.info())

# Subset the df to reveal the most commonly awarded gender and birth country
top_gender = nobel_df["sex"].value_counts().index[0]
top_country = nobel_df["birth_country"].value_counts().index[0]
print(f"The most commonly awarded gender is {top_gender}, and the top country is {top_country}.")

# Create flag column for winners whose birth country is US
nobel_df["us_winner"] = nobel_df["birth_country"] == "United States of America"
print(nobel_df["us_winner"])

# Create decade column from year column
nobel_df["decade"] = (np.floor(nobel_df["year"] / 10) * 10).astype(int)

# Get the ratio by grouping by decade column and getting the mean of the us_winner column
prop_us_win = nobel_df.groupby("decade", as_index=False)["us_winner"].mean()

# Selecting the decade with the highest proportion of US winners
max_decade_usa = prop_us_win[prop_us_win["us_winner"] == prop_us_win["us_winner"].max()]["decade"].iloc[0]

# Create a relational plot to show the proportional trend of us winners by decade
sns.set_style("whitegrid")
j = sns.relplot(x="decade", y="us_winner", data=prop_us_win, kind="line", markers=True)
j.figure.suptitle("US Winners by Decade")

# Filter for female winners
nobel_df["female_winner"] = nobel_df["sex"] == "Female"

# Group by decade and category and isolate the female_winner column, and take the mean()
prop_female_win = nobel_df.groupby(["decade", "category"], as_index=False)["female_winner"].mean()

# Filter for decade and category with the highest female winners
max_female_dec_cat = prop_female_win[prop_female_win["female_winner"] == prop_female_win["female_winner"].max()][["decade", "category"]].sort_values()
print(max_female_dec_cat)

# Create dictionary where decade is the key and category is the value.
max_female_dict = {prop_female_win["decade"].iloc[0]: prop_female_win["category"].iloc[0]}

# Create relational line plot with multiple categories
sns.set_style("whitegrid")
f = sns.relplot(x="decade", y="female_winner", data=prop_female_win, kind="line", hue="category")
f.figure.suptitle("Female Winners per Decade by Categories")

# Filter dataframe for first woman to win the Nobel Prize and in what category.
nobel_women = nobel_df[nobel_df["female_winner"]]
min_row = nobel_women[nobel_women["year"] == nobel_women["year"].min()]
first_woman_name = min_row["full_name"].iloc[0]
first_woman_category = min_row["category"].iloc[0]
print(f"The first woman to win the Nobel Prize was {first_woman_name}, in the field of {first_woman_category}.")

# Select the laureate that have received 2 or more prizes
counts = nobel_df["full_name"].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)

print("\nThe repeat winners are: ", repeat_list)