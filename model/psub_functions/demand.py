from ..behavioral.demand import market_demand_behavioral


def p_demand(_params, substep, state_history, state) -> dict:
    output = market_demand_behavioral(state, _params)
    return output
