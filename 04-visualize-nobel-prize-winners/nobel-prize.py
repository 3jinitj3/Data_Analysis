# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# import csv file and store as a dataframe
prize_data = pd.read_csv("nobel.csv")

# Filter both columns to find the top gender and top country by occurrence
top_gender = prize_data["sex"].value_counts().index[0]
top_country = prize_data["birth_country"].value_counts().index[0]

# Print top gender and top country
print("\nThe gender with the most Nobel laureates is: ", top_gender)
print("The most common birth country of Nobel laureates is: ", top_country)

# Which decade has the highest ratio of US-born Nobel Prize winners to total winners in all categorie
prize_data["us_born_winners"] = prize_data["birth_country"] == "United States of America"
prize_data["decade"] = np.floor(prize_data["year"] / 10)
prize_data["decade"] = prize_data["decade"] * 10
prize_data["decade"] = prize_data["decade"].astype(int)
prize_data_decade = prize_data.groupby("decade", as_index=False)["us_born_winners"].mean()
max_ratio = prize_data_decade["us_born_winners"].max()
max_decade_usa = prize_data_decade.loc[prize_data_decade["us_born_winners"].eq(max_ratio), "decade"].values[0]

# Plot  US Prize Winner data
sns.set_theme(style="whitegrid")
md_plot = sns.relplot(x="decade", y="us_born_winners", data=prize_data_decade, kind="line")
md_plot.figure.suptitle("US Ratio of Prize Winners by Decade")

# Which decade has the highest proportion of female laureates
prize_data["female_laureate"] = prize_data["sex"] == "Female"
female_winners_prop = prize_data.groupby(["decade", "category"], as_index=False)["female_laureate"].mean()
max_female_decade_category = female_winners_prop[female_winners_prop["female_laureate"] == female_winners_prop["female_laureate"].max()][["decade", "category"]]
max_female_dict = {max_female_decade_category["decade"].values[0]: max_female_decade_category["category"].values[0]}

# Plot Female Winners by Category data
sns.set_theme(style="whitegrid")
female_plot = sns.relplot(x="decade", y="female_laureate", hue="category", data=female_winners_prop, kind="line")
female_plot.figure.suptitle("Female Winners By Category")

# Get the first woman to win the Nobel Prize and Category
female_winners = prize_data[prize_data["female_laureate"]]
min_date = female_winners[female_winners["year"] == female_winners["year"].min()]
first_woman_name = min_date["full_name"].values[0]
first_woman_category = min_date["category"].values[0]
print(f"\nThe first woman to win a Nobel Prize was {first_woman_name}, in the category of {first_woman_category}.")

# Create a list of Winners who have won the award multiple times
counts = prize_data["full_name"].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)

print("\nThe repeat winners are :", repeat_list)
