def s_price_history(params, substep, state_history, state, _input) -> tuple:
    if 'price_history' in state.keys():
        new_history = state['price_history']+[state['price']]
    else:
        new_history=[state['price']]
    return ("price_history",new_history)

def s_ma_target(params, substep, state_history, state, _input) -> tuple:
    s = 0
    days = state['timestep']-1# TODO: check if this is the right way to get history
    days_ma = params["target_ma"]
    price_history = state['price_history']

    if days > days_ma:
        
        for i in range(days - days_ma, days):
            s += price_history[i+1]
        ma_target =  s / days_ma

    elif days ==0:
        ma_target = price_history[0]

    else:
        for i in range (0, days):
            s += price_history[i+1] # skip day 0
        s += price_history[1]* (days_ma - days)
        ma_target =  s / days_ma
    return  ("ma_target",ma_target)

