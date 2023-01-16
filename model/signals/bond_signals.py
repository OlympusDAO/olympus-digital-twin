from pandas import DataFrame
from model.types.primitives import day, OHM
from typing import List
from model.policy.ohmbond import generate_ohmbond
import numpy as np


def periodic_bond_creation(period: day, bond_tenors: List[day], face_value: OHM, simulation_timesteps: day) -> DataFrame:
    start_times = list(range(1, simulation_timesteps, period))
    face_value_temp = [[face_value] * len(bond_tenors)] * len(start_times)
    bond_tenors_temp = [bond_tenors] * len(start_times)
    bonds = generate_ohmbond(amounts=face_value_temp,
                             exp_durs=bond_tenors_temp, start_days=start_times)

    return bonds


def period_bond_creation_normal_dist(period: day, bond_tenors: List[day], face_value_mu: OHM, face_value_std: OHM, simulation_timesteps: day) -> DataFrame:
    start_times = list(range(1, simulation_timesteps, period))
    face_value_temp = np.random.normal(
        face_value_mu, face_value_std, (len(start_times), len(bond_tenors)))
    assert face_value_temp.min(
    ) >= 0, "There was a negative value for face value, check the parameters"
    face_value_temp = face_value_temp.tolist()
    bond_tenors_temp = [bond_tenors] * len(start_times)
    bonds = generate_ohmbond(amounts=face_value_temp,
                             exp_durs=bond_tenors_temp, start_days=start_times)

    return bonds
