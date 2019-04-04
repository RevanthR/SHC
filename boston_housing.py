import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

boston_dataset= load_boston()

boston =pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)

boston['MEDV']= boston_dataset.target

features=['LSTAT','RM']
target=boston['MEDV']

X=pd.DataFrame(np.c_[boston['LSTAT'],boston['RM']], columns=['LSTAT','RM'])
Y=boston['MEDV']

X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=5)



lin_model=LinearRegression()

lin_model.fit(X_train,Y_train)

Y_train_predict=lin_model.predict(X_train)

rmse=(np.sqrt(mean_squared_error(Y_train,Y_train_predict)))

r2=r2_score(Y_train,Y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
print("\n")


# model evaluation for testing set
y_test_predict = lin_model.predict(X_test)
rmse = (np.sqrt(mean_squared_error(Y_test, y_test_predict)))
r2 = r2_score(Y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print('R2 score is {}'.format(r2))
