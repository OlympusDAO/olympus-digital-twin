from .psub_functions.demand import p_demand, s_demand, s_netflow
from .psub_functions.reward_rate import p_reward_rate, s_reward_rate
from .psub_functions.amm_k import s_amm_k
from .mechanism.supply import s_supply
from .mechanism.treasury import s_treasury_stables, s_liq_backing, s_reserves_in
from .policy.treasury import p_reserves_in
from .mechanism.rbs_price import s_ma_target, s_lb_target, s_price_history, s_price_target, s_target_walls, s_target_cushions, s_bid_counter, s_ask_counter
from .policy.rbs_price import p_price_target, p_target_walls, p_target_cushions, p_bid_counter, p_ask_counter

# OVERALL TODO: check if all the order are right

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

bid_counter_block = {
    'policies': {
        'bid_counter': p_bid_counter
    },
    'variables': {
        'bid_counter': s_bid_counter
    }

}

ask_counter_block = {
    'policies': {
        'ask_counter': p_ask_counter
    },
    'variables': {
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
        'target_walls': s_target_walls
    }
}

cushions_block = {
    'policies': {
        'target_cushions': p_target_cushions
    },
    'variables': {
        'target_cushions': s_target_cushions
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

psub_blocks = [reward_rate_block,
               demand_block,
               # update variables that depend on other variables

               # update_treasury_stables
               treasury_stables_block,
               liq_backing_block,

               # update_price_history
               price_history_block,
               # ------------------RBS PRICE (based on what happened yesterday)--------------------
               # update bid_counter based on the price from yesterday
               bid_counter_block,
               # update ask_counter based on the price from yesterday
               ask_counter_block,
               # update two price targets
               price_target_block1,
               # update actual price target today
               price_target_block2,
               # update the walls around the target
               target_walls_block,
               # update the cushions around the target
               cushions_block,

               # update supply expansion based on the activities happened from yesterday, plus providing rewards
               # update_supply
               supply_block,
               # update_reserves_in
               reserves_in_block,

               # update_AMM_k_block
               amm_k_block,



               # -----------------------------------------------------
               ]
