import numpy as np
def s_price_history(params, substep, state_history, state, _input) -> tuple:
    if 'price_history' in state.keys():
        new_history = state['price_history']+[state['price']]
    else:
        new_history=[state['price']]
    return ("price_history",new_history)

# moving average target
def s_ma_target(params, substep, state_history, state, _input) -> tuple:

    days = state['timestep']-1# TODO: check if this is the right way to get history
    days_ma = params["target_ma"]
    price_history = state['price_history']

    if days > days_ma:
        
        ma_target=np.mean(price_history[-days_ma:])

    elif days ==0:
        ma_target = price_history[0]

    else:
        s = sum(price_history[1:])#  skip day 0
        s += price_history[1]* (days_ma - days)
        ma_target =  s / days_ma
    return  ("ma_target",ma_target)

# liquidity backing target
def s_lb_target(params, substep, state_history, state, _input) -> tuple:
    
    if state['supply']:
        lb_target = state['liq_backing'] / state['supply']
    else:
        lb_target=0
    return ("lb_target",lb_target)

# actual price target being used in RBS
def s_price_target(params, substep, state_history, state, _input) -> tuple:
    return ('price_target',_input['price_target'])

# walls
def s_target_walls(params, substep, state_history, state, _input) -> tuple:
    return ('target_walls',[_input['lower_target_wall'],_input['upper_target_wall']])

# cushions
def s_target_cushions(params, substep, state_history, state, _input) -> tuple:
    return ('target_cushions',[_input['lower_target_cushion'],_input['upper_target_cushion']])