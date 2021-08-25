import numpy as np
import pandas as pd

import sklearn
from sklearn.neighbors import NearestNeighbors


cars = pd.read_csv('mtcars.csv')
cars.columns = ['car_names', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()

# User specifications for the car they're looking for. They're interested in mpg, disp, hp, and wt.
t = [15, 300, 160, 3.2]
X = cars.iloc[:,[1, 3, 4, 6]].values

# Generate the recommendation using the nearest neighbor algorithm. The index value of the nearest point
# of the most similar instance in the dataset is returned.
nbrs = NearestNeighbors(n_neighbors=1).fit(X)
print(nbrs.kneighbors([t]))
