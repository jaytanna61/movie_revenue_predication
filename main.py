import numpy as np
from keras import Sequential
from keras.layers import Dropout, Dense
from sklearn import linear_model
from sklearn.svm import SVR
import pandas as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_excel('2014 and 2015 CSM dataset 2.xlsx')
X = dataset.iloc[1:, 1:-1].values
y = dataset.iloc[1:, -1].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

def lr(p):
    from sklearn import linear_model
    clf = linear_model.LinearRegression(n_jobs=-1)
    clf.fit(X, y)
    print(clf.predict(p))


def pr(X_test):
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    # transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
    X_ = sc.fit_transform(X)
    # transform the prediction to fit the model type
    predict_ = sc.transform(X_test)
    # generate the regression object
    clf = linear_model.LinearRegression()
    # preform the actual regression
    clf.fit(X_, y)
    print(clf.predict(predict_))


def ann(p):

    model = Sequential()
    model.add(Dense(14, input_dim=4, activation='relu'))
    model.add(Dropout(p=0.2))

    model.add(Dense(14, activation='relu'))
    model.add(Dropout(p=0.2))

    model.add(Dense(14, activation='relu'))
    model.add(Dropout(p=0.2))

    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='adam', metrics=['mse'])
    print model.predict(p)


mname = raw_input("Movie name")
runtime = raw_input("Movie runtime")
screen = raw_input("Number of screen movie released in")
sequl = raw_input("Number of sequal of movie")
budget = raw_input("Budget of movie")

print "linear regression output"
lr(np.array([float(runtime), float(budget), float(screen), float(sequl)]).reshape(1,-1))

print("poly regression output")
pr(np.array(np.array([float(runtime), float(budget), float(screen), float(sequl)]).reshape(1,-1)))

print("ANN output")
ann(np.array(np.array([float(runtime), float(budget), float(screen), float(sequl)]).reshape(1,-1)))