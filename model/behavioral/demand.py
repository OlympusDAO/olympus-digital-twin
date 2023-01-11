import random
from ..types import StateType, ParamsType


def market_demand_behavioral(state: StateType, params: ParamsType):
    # net_flow = random.uniform(state["treasury_stables"] * state["market_demand_supply"].total_supply,
    #                           state["treasury_stables"] * state["market_demand_supply"].total_demand)
    net_flow = random.uniform(state["liq_stables"] * state["market_demand_supply"].total_supply,
                              state["liq_stables"] * state["market_demand_supply"].total_demand) # NOTE: here changing the way to generate net_flow so that it doesn't overwhelm the liquidity. makes sense since netflow can only interact with liquidity, not the reserve (the other part of treasury)
    market_demand = params["demand_factor"] * random.uniform(0.5, 3)
    market_supply = params["supply_factor"] * random.uniform(0.5, 3)

    return {"net_flow": net_flow,
            "market_demand": market_demand,
            "market_supply": market_supply}
