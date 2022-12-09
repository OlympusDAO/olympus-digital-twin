from .psub_functions.demand import p_demand, s_demand, s_netflow
from .psub_functions.reward_rate import p_reward_rate, s_reward_rate

update_reward_rate_block = {'policies': {
    'reward_rate': p_reward_rate
},
    'variables': {
        'reward_rate': s_reward_rate,
}}

demand_update_block = {
    'policies': {
        'supply_demand': p_demand
    },
    'variables': {
        'market_demand_supply': s_demand,
        'net_flow': s_netflow
    }
}


psub_blocks = [update_reward_rate_block, demand_update_block]
