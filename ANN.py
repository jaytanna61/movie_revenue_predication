# example of training a final regression model
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
from keras.layers import Dropout


def ann():
    dataset = pd.read_excel('2014 and 2015 CSM dataset 2.xlsx')
    X = dataset.iloc[1:, 1:-1].values
    y = dataset.iloc[1:, -1].values

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X = sc.fit_transform(X)

    from sklearn.model_selection import train_test_split, GridSearchCV
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    from keras.wrappers.scikit_learn import KerasClassifier
    from sklearn.model_selection import cross_val_score
    def build_classifier():
        model = Sequential()
        model.add(Dense(14, input_dim=4, activation='relu'))
        model.add(Dropout(p=0.2))

        model.add(Dense(14, activation='relu'))
        model.add(Dropout(p=0.2))

        model.add(Dense(14, activation='relu'))
        model.add(Dropout(p=0.2))

        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='adam', metrics=['mse'])
        return model


    classifier = KerasClassifier( build_fn= build_classifier, batch_size = 10, nb_epoch = 500)
    accuracies = cross_val_score(estimator= classifier, X = X, y = y, cv=10, n_jobs=-1, scoring='neg_mean_squared_error' )
    m = accuracies.mean()

    rms = np.sqrt(-accuracies)
    print "RMSE Value : ", rms.mean()


ann()

