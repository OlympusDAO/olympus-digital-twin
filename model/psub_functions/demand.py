from ..behavioral.demand import market_demand_behavioral
from ..mechanism.demand import update_market_demand


def p_demand(_params, substep, state_history, state) -> dict:
    output = market_demand_behavioral(state, _params)
    return output


def s_demand(_params, substep, state_history, state, _input) -> dict:
    out = update_market_demand(state, _params, _input)

    return ("market_demand_supply", out)
