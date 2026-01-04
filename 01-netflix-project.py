# Start coding here! Use as many cells as you like
#Importing pandas, matplotlib, and Numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Create subset of DataFrame using the "type" column to filter movies from shows, released between 1990 & 1999
netflix_df = pd.DataFrame(netflix_df)
movies_filter_sr = netflix_df.loc[:,"type"] == "Movie" 
#_sr stands for series

movies_filter_df = netflix_df[movies_filter_sr]        
#_df stands for datafram

movies_filter_rlyr = np.logical_and(movies_filter_df["release_year"] >= 1990, movies_filter_df["release_year"] <= 1999)                                                #_rlyr stands for release year

step_one = movies_filter_df[movies_filter_rlyr]

# Filter the most frequent movie duration
plt.hist(step_one["duration"], bins=10)
plt.show()
duration = 105

# Count the number of short action movies from the 1990s
movies_filter_action_genre = step_one.loc[:,"genre"] == "Action"
genre_action_df = step_one[movies_filter_action_genre]
short_movie_count = 0
for label, row in genre_action_df.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)