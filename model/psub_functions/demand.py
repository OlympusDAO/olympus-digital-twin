from ..behavioral.demand import market_demand_behavioral


def p_demand(_params, substep, state_history, state) -> dict:
    output = market_demand_behavioral(state, _params)
    return output


def s_update_miners(_params, substep, state_history, state, _input) -> dict:

    return ("miners", _input["miners"])


# Get a mechanism that is going to return a new version of demand supply
