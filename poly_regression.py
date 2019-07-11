import numpy as np
from sklearn.svm import SVR
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn import linear_model


def poly_reg():
    dataset = pd.read_excel('2014 and 2015 CSM dataset 2.xlsx')
    X = dataset.iloc[1:, 1:-1].values
    y = dataset.iloc[1:, -1].values

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)

    y = y.reshape(-1, 1)

    ####################
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)

    # transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
    X_ = poly.fit_transform(X)
    clf = linear_model.LinearRegression()
    # preform the actual regression
    accuracies = cross_val_score(estimator=clf, X=X_, y=y, cv=10, n_jobs=-1, scoring='neg_mean_squared_error')
    m = accuracies.mean()
    rms = np.sqrt(-accuracies)
    print "RMSE Value : ", rms.mean()
    ####################

poly_reg()
####################
