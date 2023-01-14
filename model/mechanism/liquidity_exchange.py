from ..types import StateType

from ..types.primitives import USD,OHM

def ohm2stable(delta_ohm:OHM, state:StateType)->USD:
    stables = -delta_ohm *state['liq_stables']**2 / (state['amm_k'] + delta_ohm*state['liq_stables']) # is this right?? especially when there are more than 1 transactions in one step yet the liq_stables hasn't changed...
    return stables
