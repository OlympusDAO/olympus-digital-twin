from ..behavioral.ohmbond import bond_sell_batch_auction
from ..mechanism.liquidity_exchange import ohm2stable
# ==== bond creation ====

def p_bond_create(params, substep, state_history, state) -> dict:
    day = len(state_history)
    bond_create_schedule = params['bond_create_schedule']
    bondday = bond_create_schedule.loc[bond_create_schedule['start_days'] == day]
    if len(bondday):  # if today has been scheduled to create bond
        # should be a list of bond objects
        bond_create_today = bondday['bonds'].values[0]
    else:
        bond_create_today = []
    new_ohm_bonded = sum([bond.total_amount for bond in bond_create_today])
    return {'bond_created_today': bond_create_today,'new_ohm_bonded':new_ohm_bonded}


def s_bond_create(_params, substep, state_history, state, _input) -> tuple:
    existing_bonds = state['bond_created']
    return ('bond_created', existing_bonds+_input['bond_created_today'])


def s_bond_created_today(_params, substep, state_history, state, _input) -> tuple:
    return ('bond_created_today', _input['bond_created_today'])


def s_ohm_bonded(_params, substep, state_history, state, _input) -> tuple:    
    return ('ohm_bonded', state['ohm_bonded']+_input['new_ohm_bonded'])
   
def s_cum_ohm_minted_forbond(_params, substep, state_history, state, _input) -> tuple:
    
    return ('cum_ohm_minted_forbond', state['cum_ohm_minted_forbond']+_input['new_ohm_bonded'])

# ==== bond sale ====

def p_bond_sell(params, substep, state_history, state) -> dict:
    bonds_to_sell = state['bond_created_today']
    if len(bonds_to_sell):
        # assuming all bonds are sold so the only thing need to worry is how much did people pay for it
        sold_amount = bond_sell_batch_auction(
            bonds_to_sell, params["bond_annual_discount_rate"])
    else:
        sold_amount = 0
    return {'bond_sale_amount': sold_amount}

def s_liq_ohm_into_bond(_params, substep, state_history, state, _input) -> tuple:
    return ('liq_ohm_into_bond', _input['bond_sale_amount'])

def s_cum_ohm_burned_frombond(_params, substep, state_history, state, _input) -> tuple:
    return ('cum_ohm_burned_frombond', state['cum_ohm_burned_frombond']+_input['bond_sale_amount'])

def s_netflow_bondsale(_params, substep, state_history, state, _input) -> tuple:
    delta_ohm = -(_input['bond_sale_amount'] * _params['ohm_bond_to_netflow_ratio']) # when ohm bonds are sold, assuming a portion of the ohm came from the liquidity pool (i.e. users withdraw some ohm from liquidity pool to buy bonds), thus the minus sign
    return ('netflow_bondsale', ohm2stable(delta_ohm,state))


# ==== bond expiration ====

def p_bond_expire(params, substep, state_history, state) -> dict:
    day = len(state_history)
    bonds = state['bond_created']
    release_amount = 0
    for bond in bonds:
        if (bond.expiration_duration+bond.start_date) == day:  # this bond expires today!
            release_amount += bond.total_amount
    return {'ohm_released': release_amount}

def s_bond_expire(_params, substep, state_history, state, _input) -> tuple:
    return ('ohm_released', _input['ohm_released'])

def s_ohm_bonded_after_release(_params, substep, state_history, state, _input) -> tuple:

    return ('ohm_bonded', state['ohm_bonded']-_input['ohm_released'])

def s_netflow_bondexpire(_params, substep, state_history, state, _input) -> tuple:
    netflow_ohm = _input['ohm_released'] * _params['ohm_bond_to_netflow_ratio'] # when ohm bonds expire, assuming a portion of the released ohm go into the liquidity pool (i.e. users deposit some ohm into liquidity pool).

    return ('netflow_bondexpire', ohm2stable(netflow_ohm,state))

