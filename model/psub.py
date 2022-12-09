from .psub_functions.demand import p_demand, s_demand, s_netflow


demand_update_block = {
    'policies': {
        'supply_demand': p_demand
    },
    'variables': {
        'market_demand_supply': s_demand,
        'net_flow': s_netflow
    }
}


psub_blocks = [demand_update_block]
