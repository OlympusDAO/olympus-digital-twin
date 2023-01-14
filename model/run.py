import pandas as pd
import numpy as np
from .psub import psub_blocks
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
from copy import deepcopy


def load_config(monte_carlo_runs: int, params, initial_state, t):
    sim_config = config_sim({
        'N': monte_carlo_runs,  # number of monte carlo runs
        'T': list(range(t)),  # number of timesteps
        'M': params             # simulation parameters
    })

    exp = Experiment()
    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=psub_blocks
    )
    return exp


def add_config(exp: Experiment, monte_carlo_runs: int, params, initial_state, t):
    sim_config = config_sim({
        'N': monte_carlo_runs,  # number of monte carlo runs
        'T': list(range(t)),  # number of timesteps
        'M': params             # simulation parameters
    })

    exp.append_configs(
        sim_configs=sim_config,
        initial_state=initial_state,
        partial_state_update_blocks=psub_blocks
    )


def run(exp) -> pd.DataFrame:
    """
    Run simulation
    """
    # execute in local mode
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)

    sim = Executor(exec_context=local_mode_ctx, configs=exp.configs)
    raw_system_events, _, _ = sim.execute()
    df = pd.DataFrame(raw_system_events)
    return df


def post_processing(raw) -> pd.DataFrame:
    # Pull only the final substep
    df = raw.groupby(["simulation", "subset", "run",
                     "timestep"]).last().reset_index()

    # Counter values
    df["control_ask"] = df["ask_counter"].apply(lambda x: sum(x))
    df["control_bid"] = df["bid_counter"].apply(lambda x: sum(x))

    # Add a unique ID to make grouping easier
    df["unique_id"] = df["simulation"].astype(
        str) + "-" + df["subset"].astype(str) + "-" + df["run"].astype(str)

    # Backfill parameter values
    df[["demand_factor", "supply_factor", "bond_annual_discount_rate","ohm_bond_to_netflow_ratio"]] = df[[
        "demand_factor", "supply_factor", "bond_annual_discount_rate","ohm_bond_to_netflow_ratio"]].fillna(method="bfill")

    return df
