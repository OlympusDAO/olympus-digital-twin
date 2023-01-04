from ..behavioral.ohmbond import bond_sell_batch_auction
def p_bond_create(params, substep, state_history, state) -> dict:
    day = len(state_history)
    bond_create_schedule = params['bond_create_schedule']
    bondday = bond_create_schedule.loc[bond_create_schedule['start_days']==day]
    if len(bondday): # if today has been scheduled to create bond
        bond_create_today = bondday['bonds'].values[0] # should be a list of bond objects
    else:
        bond_create_today = []
    return {'bond_created_today':bond_create_today}

def s_bond_create(_params, substep, state_history, state, _input) -> tuple:
    existing_bonds = state['bond_created']
    return ('bond_created',existing_bonds+_input['bond_created_today'])

def s_bond_created_today(_params, substep, state_history, state, _input) -> tuple:
    return ('bond_created_today',_input['bond_created_today'])

def s_ohm_bonded(_params, substep, state_history, state, _input) -> tuple:
    allnewbonds = _input['bond_created_today']
    new_ohm_bonded = sum([bond.total_amount for bond in allnewbonds])
    return ('ohm_bonded',state['ohm_bonded']+new_ohm_bonded)

def s_bond_expire(_params, substep, state_history, state, _input) -> tuple:
    day = len(state_history)
    bonds = state['bond_created']
    release_amount = 0
    for bond in bonds:
        if (bond.expiration_duration+bond.start_date)==day: # this bond expires today!
            release_amount += bond.total_amount
    return ('ohm_released',release_amount)

def p_bond_sell(params, substep, state_history, state) -> dict:
    bonds_to_sell = state['bond_created_today']
    if len(bonds_to_sell):
        sold_amount = bond_sell_batch_auction(bonds_to_sell) # assuming all bonds are sold so the only thing need to worry is how much did people pay for it
    else:
        sold_amount = 0
    return {'bond_sale_amount':sold_amount}

def s_liq_ohm_into_bond(_params, substep, state_history, state, _input) -> tuple:
    return ('liq_ohm_into_bond',_input['bond_sale_amount'])