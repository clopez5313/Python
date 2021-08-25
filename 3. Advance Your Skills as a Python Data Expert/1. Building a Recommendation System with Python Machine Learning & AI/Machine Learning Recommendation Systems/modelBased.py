import numpy as np
import pandas as pd
import os

import sklearn
from sklearn.decomposition import TruncatedSVD


# Clear function for the console.
clear = lambda: os.system("cls")

columns = ['user_id', 'item_id', 'rating', 'timestamp']
frame = pd.read_csv('ml-100k/u.data', sep='\t', names=columns)
print(frame.head())
clear()

columns = ['item_id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
          'Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
          'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('ml-100k/u.item', sep='|', names=columns, encoding='latin-1')
movie_names = movies[['item_id', 'movie title']]
print(movie_names.head())
clear()

# Combine the user and movie datasets.
combined_movies_data = pd.merge(frame, movie_names, on='item_id')
print(combined_movies_data.head())
clear()

# Sort the dataset by review count.
print(combined_movies_data.groupby('item_id')['rating'].count().sort_values(ascending=False).head())
clear()

# Return the movie with most reviews.
filter = combined_movies_data['item_id']==50
print(combined_movies_data[filter]['movie title'].unique())
clear()

# Build a utility matrix.
rating_crosstab = combined_movies_data.pivot_table(values='rating', index='user_id', columns='movie title', fill_value=0)

# Transpose the matrix.
X = rating_crosstab.T

# Decompose the transposed matrix to obtain some generalized user tastes. (discover latent variables about users)
SVD = TruncatedSVD(n_components=12, random_state=17)
resultant_matrix = SVD.fit_transform(X)

# Generate a correlation matrix.
corr_mat = np.corrcoef(resultant_matrix)

# Isolating Star-Wars (the movie with most reviews) from the matrix.
movie_names = rating_crosstab.columns
movies_list = list(movie_names)
star_wars = movies_list.index('Star Wars (1977)')
corr_star_wars = corr_mat[star_wars]

# Recommending highly-correlated movies.
print(list(movie_names[(corr_star_wars<1.0) & (corr_star_wars > 0.9)]))
print()
print(list(movie_names[(corr_star_wars<1.0) & (corr_star_wars > 0.95)]))
