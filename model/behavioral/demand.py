import random


def market_demand_behavioral(state, params):
    net_flow = random.uniform(state["treasury"] * state["total_supply"],
                              state["treasury"] * state["total_demand"])
    market_demand = params["demand_factor"] * random.uniform(0.5, 3)
    market_supply = params["supply_factor"] * random.uniform(0.5, 3)

    return {"net_flow": net_flow,
            "market_demand": market_demand,
            "market_supply": market_supply}
