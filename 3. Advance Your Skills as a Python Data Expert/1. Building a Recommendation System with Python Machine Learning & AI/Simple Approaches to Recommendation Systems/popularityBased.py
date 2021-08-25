import pandas as pd
import numpy as np
import os


frame = pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')

# Clear function for the console.
clear = lambda: os.system("cls")

# Returns a table with user reviews to different restaurants.
print(frame.head())
clear()

# Returns a table with restaurant IDs and the type of food they serve.
print(cuisine.head())
clear()

# Making recommendations based on the amount of ratings (reviews).
rating_count = pd.DataFrame(frame.groupby('placeID')['rating'].count())
print(rating_count.sort_values('rating', ascending=False).head())
clear()

# Check the top 5 places with most reviews and determine what type of food they serve.
most_rated_places = pd.DataFrame([135085, 132825, 135032, 135052, 132834], index=np.arange(5), columns=['placeID'])
summary = pd.merge(most_rated_places, cuisine, on='placeID')
print(summary)
clear()

# Show information about the type of food attribute.
print(cuisine['Rcuisine'].describe())
