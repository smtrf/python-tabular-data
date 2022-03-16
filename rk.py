#! /usr/bin/env python3

"A module for plotting regression in python."

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

import sys


def get_flower_size_plot():
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

if __name__ == '__main__':
    get_flower_size_plot()
