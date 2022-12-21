from .psub_functions.demand import p_demand, s_demand, s_netflow
from .psub_functions.reward_rate import p_reward_rate, s_reward_rate
from .psub_functions.amm_k import s_amm_k
from .mechanism.supply import s_supply
from .mechanism.treasury import s_treasury_stables, s_liq_backing, s_reserves_in
from .policy.treasury import p_reserves_in
from .mechanism.rbs_price import s_ma_target, s_lb_target, s_price_history, s_price_target, s_upper_target_wall, s_lower_target_wall, s_lower_target_cushion, s_upper_target_cushion, s_bid_counter, s_ask_counter
from .policy.rbs_price import p_price_target, p_target_walls, p_target_cushions, p_bid_counter, p_ask_counter
from .psub_functions.target_capacity import p_target_capacity, s_bid_capacity_target, s_ask_capacity_target, s_bid_capacity_target_cushion, s_ask_capacity_target_cushion, s_natural_price
from .psub_functions.treasury_market_operations import (p_real_bid_capacity_cushion, p_real_ask_capacity_cushion, s_bid_capacity_cushion, s_ask_capacity_cushion,
                                                        p_effective_bid_capacity_cushion, p_effective_ask_capacity_cushion, s_bid_change_cushion_usd, s_bid_change_cushion_ohm, s_ask_change_cushion_usd, s_ask_change_cushion_ohm,
                                                        p_real_bid_capacity_totals, p_real_ask_capacity_totals, s_bid_capacity, s_ask_capacity,
                                                        p_effective_bid_capacity_changes_totals, p_effective_ask_capacity_changes_totals, s_bid_change_ohm, s_bid_change_usd, s_ask_change_ohm, s_ask_change_usd
                                                        )

reward_rate_block = {'policies': {
    'reward_rate': p_reward_rate
},
    'variables': {
        'reward_rate': s_reward_rate,
}}

demand_block = {
    'policies': {
        'supply_demand': p_demand
    },
    'variables': {
        'market_demand_supply': s_demand,
        'net_flow': s_netflow
    }
}

treasury_stables_block = {  # Warning: this part is actually "treasury_stables from yesterday"
    "policies": {},
    "variables": {
        "treasury_stables": s_treasury_stables
    }
}

liq_backing_block = {  # Warning: this part is actually "treasury_stables from yesterday"
    "policies": {},
    "variables": {
        "liq_backing": s_liq_backing
    }
}

price_history_block = {
    "policies": {},
    "variables": {
        "price_history": s_price_history
    }
}

reinstate_counter_block = {
    'policies': {
        'bid_counter': p_bid_counter,
        'ask_counter': p_ask_counter
    },
    'variables': {
        'bid_counter': s_bid_counter,
        'ask_counter': s_ask_counter
    }

}


price_target_block1 = {
    'policies': {},
    'variables': {
        'ma_target': s_ma_target,
        'lb_target': s_lb_target,
    }
}

price_target_block2 = {
    'policies': {
        'price_target': p_price_target
    },
    'variables': {
        'price_target': s_price_target,
    }
}

target_walls_block = {
    'policies': {
        'target_walls': p_target_walls
    },
    'variables': {
        'upper_target_wall': s_upper_target_wall,
        "lower_target_wall": s_lower_target_wall
    }
}

cushions_block = {
    'policies': {
        'target_cushions': p_target_cushions
    },
    'variables': {
        'lower_target_cushion': s_lower_target_cushion,
        'upper_target_cushion': s_upper_target_cushion
    }
}


supply_block = {
    'policies': {

    },
    'variables': {
        'supply': s_supply
    }
}


reserves_in_block = {
    'policies': {
        "reserves_in": p_reserves_in
    },
    'variables': {
        'reserves_in': s_reserves_in
    }
}

amm_k_block = {
    'policies': {},
    'variables': {
        'amm_k': s_amm_k,  # Note: for now it's actually constant k
    }
}

target_capacities_block = {
    'policies': {
        "target_capacity": p_target_capacity
    },
    'variables': {
        "bid_capacity_target": s_bid_capacity_target,
        "ask_capacity_target": s_ask_capacity_target,
        "bid_capacity_target_cushion": s_bid_capacity_target_cushion,
        "ask_capacity_target_cushion": s_ask_capacity_target_cushion,
        "natural_price": s_natural_price, }
}

real_capacity_cushion_block = {'policies': {
    "real_bid_capacity_cushion": p_real_bid_capacity_cushion,
    "real_ask_capacity_cushion": p_real_ask_capacity_cushion
},
    'variables': {
        "bid_capacity_cushion": s_bid_capacity_cushion,
        "ask_capacity_cushion": s_ask_capacity_cushion, }}

effective_capacity_cushion_block = {'policies': {
    "effective_bid_capacity_cushion": p_effective_bid_capacity_cushion,
    "effective_ask_capacity_cushion": p_effective_ask_capacity_cushion
},
    'variables': {
        "bid_change_cushion_usd": s_bid_change_cushion_usd,
        "bid_change_cushion_ohm": s_bid_change_cushion_ohm,
        "ask_change_cushion_usd": s_ask_change_cushion_usd,
        "ask_change_cushion_ohm": s_ask_change_cushion_ohm, }}


real_capacity_totals_block = {'policies': {
    "real_bid_capacity_totals": p_real_bid_capacity_totals,
    "real_ask_capacity_totals": p_real_ask_capacity_totals
},
    'variables': {
        "bid_capacity_cushion": s_bid_capacity_cushion,
        "bid_capacity": s_bid_capacity,
        "ask_capacity_cushion": s_ask_capacity_cushion,
        "ask_capacity": s_ask_capacity, }}

effective_capacity_changes_totals_block = {'policies': {
    "effective_bid_capacity_changes_totals": p_effective_bid_capacity_changes_totals,
    "effective_ask_capacity_changes_totals": p_effective_ask_capacity_changes_totals
},
    'variables': {
        "bid_change_ohm": s_bid_change_ohm,
        "bid_change_usd": s_bid_change_usd,
        "ask_change_ohm": s_ask_change_ohm,
        "ask_change_usd": s_ask_change_usd, }}


psub_blocks = [treasury_stables_block, liq_backing_block, reward_rate_block, supply_block, reserves_in_block, amm_k_block,
               price_target_block1, price_target_block2, target_walls_block, cushions_block,
               reinstate_counter_block, demand_block, target_capacities_block, real_capacity_cushion_block,
               effective_capacity_cushion_block, real_capacity_totals_block, effective_capacity_changes_totals_block,
               price_history_block]
