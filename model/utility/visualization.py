from typing import List
from pandas import DataFrame
import matplotlib.pyplot as plt


def plot_all_sims(var_list: List[str], df: DataFrame):
    for col in var_list:
        df.pivot("timestep", "unique_id", col).plot(kind='line')
        plt.title(col)
        plt.legend([])
        plt.show()


def plot_grouped_variables_average(var_list: List[str], grouping_variables: List[str], df: DataFrame):
    data = df.groupby(grouping_variables + ["timestep"])[var_list].mean()
    for col in var_list:
        data[col].unstack(-1).T.plot(kind='line')
        plt.title(col)
        plt.show()
