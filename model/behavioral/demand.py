import random
from ..types import StateType, ParamsType

import numpy as np
def panic_sell_amount(price_change,liq_ohm,L=1,k=1,p0=3):
    # given the price change, how much sell will happen. right now it's governed by a logistic function
    # L is the scaling magnitude controller, ranging (0,+inf). higher L => higher ceiling
    # k is the factor adjusting the curve shape, ranging (0,+inf). bigger k => sharper increase of the sell amount
    # p0 is the turning point when the sell amount increases the fastest

    # TODO: in the future, allow different shapes of this curve 
    if price_change>=0:
        return 0
    else:
        max_amount = liq_ohm*(L/(1+np.exp(-k*(np.abs(price_change)-p0)))) # the max amount of sell given the price change is determined by a logistic function
        # turn it into a uniform distribution for each instance to introduce more randomness
        randamount = (np.random.rand()*.8+.2)*max_amount # ranging between 0.2 to 1 times of the max_amount
        if randamount > liq_ohm:
            randamount = liq_ohm
        return randamount
def market_demand_behavioral(state: StateType, params: ParamsType):
    # net_flow = random.uniform(state["treasury_stables"] * state["market_demand_supply"].total_supply,
    #                           state["treasury_stables"] * state["market_demand_supply"].total_demand)
    net_flow = random.uniform(state["liq_stables"] * state["market_demand_supply"].total_supply,
                              state["liq_stables"] * state["market_demand_supply"].total_demand) # NOTE: here changing the way to generate net_flow so that it doesn't overwhelm the liquidity. makes sense since netflow can only interact with liquidity, not the reserve (the other part of treasury)
    market_demand = params["demand_factor"] * random.uniform(0.5, 3)
    market_supply = params["supply_factor"] * random.uniform(0.5, 3)

    if params['panic_sell_on']:
        liq_stables = state['liq_stables']
        if len(state['price_history'])<2:
            price_change=0
        else:
            price_change = state['price_history'][-1] - state['price_history'][-2]
        net_flow -= panic_sell_amount(price_change,liq_stables,params['panic_param']) # panic selling ohm => decrease of stables in the pool

        

    return {"net_flow": net_flow,
            "market_demand": market_demand,
            "market_supply": market_supply}
