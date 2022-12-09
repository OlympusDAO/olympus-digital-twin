from .primitives import USD, PlaceholderTypeDemandSupply
from typing import TypedDict

StateType = TypedDict('StateType', {
                      'treasury': USD, 'total_supply': PlaceholderTypeDemandSupply, 'total_demand': PlaceholderTypeDemandSupply})
ParamsType = TypedDict('ParamsType', {
                       'demand_factor': PlaceholderTypeDemandSupply, 'supply_factor': PlaceholderTypeDemandSupply})
