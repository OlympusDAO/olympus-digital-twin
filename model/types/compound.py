from dataclasses import dataclass
from .primitives import PlaceholderTypeDemandSupply


@dataclass
class MarketDemandSupply:
    total_supply: PlaceholderTypeDemandSupply
    total_demand: PlaceholderTypeDemandSupply
