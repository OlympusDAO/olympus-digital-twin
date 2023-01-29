from typing import List
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from .ohmbond_metrics import get_price_standard_deviation

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


def plot_price_standard_deviation(df:DataFrame):
    # TODO: allow different ways to group simulations (now it's based on bond_schedule)
    av_std,se_of_std = get_price_standard_deviation(df)
    plt.bar(x=np.arange(len(av_std)),height=av_std)
    plt.errorbar(x=np.arange(len(av_std)),y=av_std,yerr=se_of_std,color='k')
    plt.xticks(ticks=np.arange(len(av_std)),labels=df['bond_schedule_name'].dropna().unique(),rotation=45)
    plt.ylabel('average standard deviation in the run')
    plt.show()

def plot_price_standard_deviation_multiple_exps(exps:List[dict]):
    # TODO: allow different ways to group simulations (now it's based on bond_schedule)
    means = {}
    ses = {}
    for exp in exps:
        df = exp['df']
        exp_label = exp['label']
        av_std,se_of_std = get_price_standard_deviation(df)
        means[exp_label]=av_std
        ses[exp_label]=se_of_std
    means_df = DataFrame(means,index = df['bond_schedule_name'].dropna().unique())
    ses_df = DataFrame(ses,index = df['bond_schedule_name'].dropna().unique())

    fig, ax = plt.subplots()
    means_df.plot.bar(yerr=ses_df, ax=ax, capsize=4, rot=-45)
    fig.show()

def get_interruption_rate(df,totalstep:int)-> DataFrame:
    maxstep = df.groupby([ "subset","run"]).timestep.max()
    r_interrupt = (maxstep<totalstep).groupby("subset").mean()
    return r_interrupt
def plot_simu_interruption_rate(df,number_steps:int):
    interrupt_rate = get_interruption_rate(df,number_steps)
    print(interrupt_rate)
    plt.bar(np.arange(len(interrupt_rate)),interrupt_rate)
    plt.xticks(ticks=np.arange(len(interrupt_rate)),labels=df['bond_schedule_name'].dropna().unique(),rotation=-45)
    plt.ylabel('average rate of a run unfinished')
    plt.show()
def plot_simu_interruption_rate_multiple_exps(exps:List[dict],number_steps:int):
    all_r_interrupt = {}
    for exp in exps:
        df = exp['df']
        exp_label = exp['label']
        interrupt_rate = get_interruption_rate(df,number_steps)
        all_r_interrupt[exp_label] = np.array(interrupt_rate)
    all_r_interrupt_df = DataFrame(all_r_interrupt,index = df['bond_schedule_name'].dropna().unique())
    fig, ax = plt.subplots()
    all_r_interrupt_df.plot.bar(ax=ax, capsize=4, rot=-45)
    fig.show()
