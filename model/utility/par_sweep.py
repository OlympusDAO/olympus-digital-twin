from itertools import product

def create_par_sweep(sweep_dict:dict):
    sweeps = list(product(*sweep_dict.values()))
    for kk, varname in enumerate(sweep_dict.keys()):
        sweep_dict[varname]=[x[kk] for x in sweeps]
    return sweep_dict