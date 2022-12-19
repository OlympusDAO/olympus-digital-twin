
from ..types.primitives import USD,OHM
def treasury_stables_mechanism(liq,reserve)->USD:
    return liq + reserve
def s_treasury_stables(params, substep, state_history, state,_input) -> tuple:
    return ("treasury_stables",treasury_stables_mechanism(state['liq_stables'],state['reserves_stables']))

def liq_ohm_mechanism(liq_stables,price)->OHM:
    return liq_stables / price

def floating_supply_mechanism(supply,liq_ohm)->OHM:
    return  max(supply - liq_ohm, 0)

def s_floating_supply(params,substep, state_history, state,_input) -> tuple:
    return floating_supply_mechanism(state['supply'],state['liq_ohm'])

def liq_backing_mechanism(stables,volatiles)->USD:
    return stables + volatiles
def s_liq_backing(params,substep, state_history, state,_input) -> tuple:
    return ("liq_backing",liq_backing_mechanism(state['treasury_stables'] ,params['initial_reserves_volatile']))
    
def s_reserves_in(params, substep, state_history, state,_input) -> tuple:
    return ("reserves_in",_input['reserves_in'])
