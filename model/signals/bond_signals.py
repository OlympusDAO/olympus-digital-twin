from pandas import DataFrame
from model.types.primitives import day, OHM
from typing import List
from model.policy.ohmbond import generate_ohmbond
import numpy as np


def periodic_bond_creation(period: day, bond_tenors: List[day], face_value: OHM, simulation_timesteps: day) -> DataFrame:
    """Creates a signal of bond creations where every number of days (period),
    bonds of all tenors listed will be created all with the same face value specified

    Args:
        period (day): The periodic number of days for bond creation
        bond_tenors (List[day]): The tenors for the bonds to create
        face_value (OHM): The face value that all bonds will have
        simulation_timesteps (day): The number of timesteps the simulation has

    Returns:
        DataFrame: A DataFrame of bonds to be created and the time at which they will be created
    """
    # List of start times for bond release
    start_times = list(range(1, simulation_timesteps, period))

    # The face values that the bonds will have
    face_value_temp = [[face_value] * len(bond_tenors)] * len(start_times)

    # The tenors that the bonds will have
    bond_tenors_temp = [bond_tenors] * len(start_times)

    # Generate the bonds
    bonds = generate_ohmbond(amounts=face_value_temp,
                             exp_durs=bond_tenors_temp, start_days=start_times)

    return bonds


def period_bond_creation_normal_dist(period: day, bond_tenors: List[day], face_value_mu: OHM, face_value_std: OHM, simulation_timesteps: day) -> DataFrame:
    """Creates a signal of bond creations where every number of days (period),
    bonds of all tenors listed will be created all with a face value pulled
    from the normal distribution governed by the parameters for face_value_mu,
    and face_value_std

    Args:
        period (day): The periodic number of days for bond creation
        bond_tenors (List[day]): The tenors for the bonds to create
        face_value_mu (OHM): The average face value of the bonds
        face_value_std (OHM): The standard deviation of the face value of bonds
        simulation_timesteps (day): The number of timesteps the simulation has

    Returns:
        DataFrame: A DataFrame of bonds to be created and the time at which they will be created
    """
    # List of start times for bond release
    start_times = list(range(1, simulation_timesteps, period))

    # Face values the bonds will have pulled from a normal distribution
    face_value_temp = np.random.normal(
        face_value_mu, face_value_std, (len(start_times), len(bond_tenors)))
    assert face_value_temp.min(
    ) >= 0, "There was a negative value for face value, check the parameters"

    # Convert the numpy array to a list
    face_value_temp = face_value_temp.tolist()

    # The tenors the bonds will have
    bond_tenors_temp = [bond_tenors] * len(start_times)

    # Create the bonds
    bonds = generate_ohmbond(amounts=face_value_temp,
                             exp_durs=bond_tenors_temp, start_days=start_times)

    return bonds
