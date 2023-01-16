from pandas import DataFrame
from model.types.primitives import day, OHM
from typing import List
from model.policy.ohmbond import generate_ohmbond


def periodic_bond_creation(period: day, bond_tenors: List[day], face_value: OHM, simulation_timesteps: day) -> DataFrame:
    start_times = list(range(1, simulation_timesteps, period))
    face_value_temp = [[face_value] * len(bond_tenors)] * len(start_times)
    bond_tenors_temp = [bond_tenors] * len(start_times)
    bonds = generate_ohmbond(amounts=face_value_temp,
                             exp_durs=bond_tenors_temp, start_days=start_times)

    return bonds
