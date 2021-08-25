import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


bank_full = pd.read_csv('bank_full_w_dummy_vars.csv')

# Define the columns that will be used to train the model. Also define the predicted variable.
X = bank_full.iloc[:,[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]].values
y = bank_full.iloc[:,17].values

# Build and train the model.
LogReg = LogisticRegression()
LogReg.fit(X, y)
y_pred = LogReg.predict(X)

# Print the results of the model performance.
print(classification_report(y, y_pred))
