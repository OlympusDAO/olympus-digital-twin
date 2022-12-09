from .primitives import USD, PlaceholderTypeDemandSupply
from typing import TypedDict
from .compound import MarketDemandSupply

StateType = TypedDict('StateType', {
                      'treasury': USD,
                      'market_demand_supply': MarketDemandSupply,
                      "net_flow": PlaceholderTypeDemandSupply})
ParamsType = TypedDict('ParamsType', {
                       'demand_factor': PlaceholderTypeDemandSupply, 'supply_factor': PlaceholderTypeDemandSupply})