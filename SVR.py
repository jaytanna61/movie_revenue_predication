import numpy as np
from sklearn.svm import SVR
import pandas as pd

def my_svr():
    x = np.array([95, 175000000, 3946, 1])
    x = x.reshape(1, -1)

    dataset = pd.read_excel('2014 and 2015 CSM dataset 2.xlsx')
    X = dataset.iloc[1:, 1:-1].values
    y = dataset.iloc[1:, -1].values
   #y = y.reshape(1,-1)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)
    x = sc.transform(x)


    from sklearn.model_selection import train_test_split, GridSearchCV
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
    from sklearn import linear_model
    clf = linear_model.LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)



    confidence = clf.score(X_test, y_test)
    print clf.coef_
    print(confidence)



    ####################



    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree=2)
    # transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
    X_ = poly.fit_transform(X_train)
    print X_
    # transform the prediction to fit the model type
    predict_ = poly.fit_transform(X_test)
    # generate the regression object
    clf = linear_model.LinearRegression()
    # preform the actual regression
    clf.fit(X_, y_train)



    print clf.coef_
    confidence = clf.score(predict_, y_test)
    print confidence
    print y.mean()
    ####################

my_svr()
####################
