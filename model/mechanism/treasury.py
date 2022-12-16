def s_treasury_stables(params, substep, state_history, state,_input) -> dict:
    return ("treasury_stables",state['liq_stables']+state['reserves_stables'])
    
def s_reserves_in(params, substep, state_history, state,_input) -> dict:
    return ("reserves_in",_input['reserves_in'])