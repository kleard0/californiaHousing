# -*- coding: utf-8 -*-
"""californiaHousing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g6iHxToirddE7CmUnT44B_CSUuhDxU87

# Import des bibliotèques
"""

import numpy as np
import matplotlib.pyplot as plt # pr la visualisation
import pandas as pd

from sklearn.datasets import fetch_california_housing # le dataset

"""# On charge notre dataset"""

housing = fetch_california_housing() #chargement du dataset

X = pd.DataFrame(housing.data, columns=housing.feature_names)
# dataframe des features
y = pd.Series(housing.target)
# Series prix de maison (target)

"""# On vérifie notre dataset



"""

print("Features")
print(X.head()) # première ligne dataframe
print("Cible")
print(y.head())

"""# On vérifie les valeurs null




"""

print("feature")
print(X.isnull().sum()) # compte le nombre de valeur null par colonne
print("Cible")
print(y.isnull().sum())

"""# On sépare les données d'entrainement et de test

70% d'entrainemente et 30% de test
"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
# separation donnée de train et de test

"""# Regression linéaire"""

from sklearn.linear_model import LinearRegression
# import model regression
LinearRegression = LinearRegression()
LinearRegression.fit(X_train, y_train)
#entraiment du modèle sur les donnée de train

c = LinearRegression.intercept_
print(c) # ordonné à l'origine (intercept)
m = LinearRegression.coef_
print(m) # coef de regression (pente) pour chaque caractéristique

"""# Prédiction


"""

y_pred_train = LinearRegression.predict(X_train)
# prédiction sur les donnée d'entrainement
print(y_pred_train)

import matplotlib.pyplot as plt
# visualisation des prédiction sur les données d'entrainement
plt.scatter(y_train, y_pred_train)
plt.xlabel("Valeurs réelles")
plt.ylabel("Valeurs prédites")
plt.title("Comparaison des valeurs réelles et prédites")
plt.show()

from sklearn.metrics import r2_score
r2_score(y_train, y_pred_train)

y_pred_train = LinearRegression.predict(X_test)

import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred_train)
plt.xlabel("Valeurs réelles")
plt.ylabel("Valeurs prédites")
plt.title("Comparaison des valeurs réelles et prédites")

print(r2_score(y_test, y_pred_train))

