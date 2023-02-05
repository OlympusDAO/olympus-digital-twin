import random
from ..types import StateType, ParamsType

import numpy as np
def panic_sell_amount(price_change,liq_stables,k=0.1,sigma=.05):
    # given the price change, how much sell will happen
    # k is the factor adjusting the curve shape, ranging (0,+inf)
    # TODO: in the future, allow different shapes of this curve (e.g. sigmoid)
    if price_change>=0:
        return 0
    else:
        amount = liq_stables*(1-np.exp(-k*np.abs(price_change)))
        # turn it into log normal distribution
        mu  = np.log(amount) + sigma ** 2 # so the mode for this random distribution is 
        rng = np.random.default_rng()
        randamount = rng.lognormal(mu, sigma, 1)[0]
        #randamount = np.random.lognormal(mu,sigma)
        if randamount > liq_stables:
            randamount = liq_stables
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
