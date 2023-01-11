from typing import List
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


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
    return plt.figure

def plot_multivars_grouped_average(var_list: list[str], grouping_variables: list[str], df: DataFrame,linestyles:list=[]):
    grpvar_vals = np.unique(df[grouping_variables],axis=0)
    data = df.groupby(grouping_variables + ["timestep"])[var_list].mean()#.reset_index(grouping_variables)
    fig,axes = plt.subplots(nrows=len(grpvar_vals),figsize=(4*len(grpvar_vals),20))

    if len(linestyles)==0:
        linestyles = ['-'] * len(var_list)
    for k,ax in enumerate(axes):
        for plotvar,lstyle in zip(var_list,linestyles):
            ax.plot(data[plotvar].unstack(-1).T[tuple(grpvar_vals[k])],label=plotvar,linestyle = lstyle)
            ax.legend()
        titlestr = ''
        for var,varval in zip(grouping_variables,grpvar_vals[k]):
            titlestr += f'{var} = {varval}, '
        ax.set_title(titlestr[:-2])
    fig.show()
    return fig
