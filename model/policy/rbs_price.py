def p_price_target(params, substep, state_history, state) -> dict:
    return {'price_target':max(state['ma_target'],state['lb_target'])}
def p_target_walls(params, substep, state_history, state) -> dict:
    return {'lower_target_wall',lower_target_policy(state['price_target'] , params['lower_wall']),
            'upper_target_wall',upper_target_policy(state['price_target'], params['upper_wall'])}
def p_target_cushions(params, substep, state_history, state) -> dict:
    return {'lower_target_cushion',lower_target_policy(state['price_target'] , params['lower_cushion']),
            'upper_target_cushion',upper_target_policy(state['price_target'], params['upper_cushion'])}
def lower_target_policy(price_target,lower_factor):
    return price_target*(1-lower_factor)
def upper_target_policy(price_target,upper_factor):
    return price_target*(1+upper_factor)
