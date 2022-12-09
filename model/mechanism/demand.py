from ..types import StateType, ParamsType
from ..types import MarketDemandSupply


def update_market_demand(state: StateType, params: ParamsType, _input):
    out = MarketDemandSupply(total_supply=_input["market_supply"],
                             total_demand=_input["market_demand"])

    return out
