from itertools import product
from copy import deepcopy
from model.types.config import ParamsType


def create_par_sweep(sweep_dict: dict) -> dict:
    """This function takes a dictionary where key is parameter name
    and value is a list of all possible values for that parameter. It
    converts this into a dictionary with the same keys but with values
    that are the cartesian product of all the lists.

    Args:
        sweep_dict (dict): A dictionary of params and values to sweep over

    Returns:
        dict: A dictionary of cartesian product params
    """
    # Copy sweep_dict to avoid overwriting
    sweep_dict = deepcopy(sweep_dict)

    # Get the cartesian product
    sweeps = list(product(*sweep_dict.values()))

    # Assign values
    for kk, varname in enumerate(sweep_dict.keys()):
        sweep_dict[varname] = [x[kk] for x in sweeps]

    return sweep_dict


def create_par_sweep_and_apply(sweep_dict: dict, params: ParamsType) -> None:
    """Create the cartesian parameter sweep dictionary and then overwrite the values
    for params

    Args:
        sweep_dict (dict): A dictionary of params and values to sweep over
        params (ParamsType): The parameters of the system
    """

    # Get the param sweep
    sweep_dict = create_par_sweep(sweep_dict)

    # Update params
    for key in sweep_dict.keys():
        params[key] = sweep_dict[key]
