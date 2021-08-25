import numpy as np
import pandas as pd
import os

from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression


# Clear function for the console.
clear = lambda: os.system("cls")

bank_full = pd.read_csv('bank_full_w_dummy_vars.csv')
# print(bank_full.head())

# Returns a description of the dataset.
# print(bank_full.info())

# Define the columns that will be used to train the model. Also define the predicted variable.
X = bank_full.iloc[:,18:37].values
y = bank_full.iloc[:,17].values

# Build and train the model.
LogReg = LogisticRegression()
LogReg.fit(X, y)

# Display the results.
new_user = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
y_pred = LogReg.predict(new_user)

if y_pred == 0:
    print("The customer won't accept the offer.")
else:
    print("The customer will accept the offer.")
