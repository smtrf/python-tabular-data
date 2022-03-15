#! /usr/bin/env python3

"A script for plotting in python."

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
dataframe = pd.read_csv("iris.csv")
versicolor = dataframe[dataframe.species == "Iris_versicolor"]
x = versicolor.petal_length_cm
y = versicolor.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("versicolor_petal_v_sepal_length_regress.png")
plt.clf()

dataframe2 = pd.read_csv("iris.csv")
setosa = dataframe2[dataframe2.species == "Iris_setosa"]
x = setosa.petal_length_cm
y = setosa.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("setosa_petal_v_sepal_length_regress.png")
plt.clf()


dataframe3 = pd.read_csv("iris.csv")
virginica = dataframe3[dataframe3.species == "Iris_virginica"]
x = virginica.petal_length_cm
y = virginica.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("virginica_petal_v_sepal_length_regress.png")
plt.clf()
quit()


