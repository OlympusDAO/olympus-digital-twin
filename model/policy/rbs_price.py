def p_price_target(_params, substep, state_history, state) -> dict:
    return {'price_target':max(state['ma_target'],state['lb_target'])}