# Import pandas
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
print(schools.head())

# Finding schools with the best math scores (80% of 800 >= 640)

# Subset .df by average_math being greater than or equal to 640 and sort in descending order.
best_math_schools = schools[schools["average_math"] > 640][["school_name", "average_math"]].sort_values(by="average_math", ascending=False)

print(best_math_schools)

# What are the top 10 performing schools based on the combined SAT scores?

# Create new column total_SAT to hold sum of 3 categories
schools["total_SAT"] = schools["average_math"] + schools["average_writing"] + schools["average_reading"]

#Subst the top 10 schools by total SAT score, sort in descending order.
top_10_schools = schools[["school_name", "total_SAT"]].sort_values(by="total_SAT", ascending=False).head(10)

print(top_10_schools)

# Which school has the largest STD in the combined SAT score?

# Subset to get borough column with total_SAT values (count, mean, std) rounded to nearest 2 decimals
boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

# Filter to get max std
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename columns for descriptive presentation
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Reset indexes back to columns
largest_std_dev.reset_index(inplace=True)

print(largest_std_dev)