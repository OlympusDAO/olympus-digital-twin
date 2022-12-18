from .primitives import USD,OHM,day, PlaceholderTypeDemandSupply
from typing import TypedDict
from .compound import MarketDemandSupply

StateType = TypedDict('StateType', {
                      'reward_rate':float,
                      'liq_stables':USD,
                      'reserves_stables':USD,
                      'treasury_stables':USD,
                      'liq_backing':USD,
                    #   'price':USD/OHM,
                    #   'ma_target':USD/OHM,
                      'reserves_in':USD,
                      'target_liq_ratio_reached':bool,
                      'ask_change_ohm':OHM,
                      'bid_change_ohm':OHM,
                      'market_demand_supply': MarketDemandSupply,
                      "net_flow": USD})
ParamsType = TypedDict('ParamsType', {
                        'target_ma':day,
                        'demand_factor': PlaceholderTypeDemandSupply, 'supply_factor': PlaceholderTypeDemandSupply})
