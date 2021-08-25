import numpy as np
import pandas as pd
import os


frame =  pd.read_csv('rating_final.csv')
cuisine = pd.read_csv('chefmozcuisine.csv')
geodata = pd.read_csv('geoplaces2.csv', encoding = 'mbcs')

# Clear function for the console.
clear = lambda: os.system("cls")

# Restaurant data with richer information.
print(geodata.head())
clear()

# Retrieve only the ID and name columns.
places =  geodata[['placeID', 'name']]
print(places.head())
clear()

# Get the mean value ratings for the restaurants.
rating = pd.DataFrame(frame.groupby('placeID')['rating'].mean())
print(rating.head())
clear()

# Add a column to the table that display the count of reviews (ratings).
rating['rating_count'] = pd.DataFrame(frame.groupby('placeID')['rating'].count())
print(rating.head())
clear()

# Returns statistical data of the dataset.
print(rating.describe())
clear()

# Returns the places with the most reviews.
print(rating.sort_values('rating_count', ascending=False).head())
clear()

# Returns the name and the type of food served by the restaurant with the most reviews.
print(places[places['placeID']==135085])
clear()
print(cuisine[cuisine['placeID']==135085])
clear()

# Build an user-by-item utility matrix.
places_crosstab = pd.pivot_table(data=frame, values='rating', index='userID', columns='placeID')
# print(places_crosstab.head())

# Display the ratings given to the restaurant with the most reviews.
Tortas_ratings = places_crosstab[135085]
# print(Tortas_ratings[Tortas_ratings>=0])

# Find the correlation between the restaurant with most reviews and the rest of restaurants.
# Correlation is based on similarities and user reviews that were given to each place.
similar_to_Tortas = places_crosstab.corrwith(Tortas_ratings)

corr_Tortas = pd.DataFrame(similar_to_Tortas, columns=['PearsonR'])
corr_Tortas.dropna(inplace=True)
print(corr_Tortas.head())
clear()

# The correlation results have to be filtered so the places with more reviews have more weight.
Tortas_corr_summary = corr_Tortas.join(rating['rating_count'])

# Return the top 10 most correlated restaurants, for a review count greater or equal than 10.
print(Tortas_corr_summary[Tortas_corr_summary['rating_count']>=10].sort_values('PearsonR', ascending=False).head(10))
clear()

# Return the top 7 correlated results and see whether any of them serve Fast Food.
places_corr_Tortas = pd.DataFrame([135085, 132754, 135045, 135062, 135028, 135042, 135046], index = np.arange(7), columns=['placeID'])
summary = pd.merge(places_corr_Tortas, cuisine,on='placeID')
print(summary)
