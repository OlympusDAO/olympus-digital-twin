from dataclasses import dataclass
from .primitives import PlaceholderTypeDemandSupply,day,OHM


@dataclass
class MarketDemandSupply:
    total_supply: PlaceholderTypeDemandSupply
    total_demand: PlaceholderTypeDemandSupply

@dataclass
class OHMbond:
    total_amount: OHM
    expiration_duration: day
    start_date:day
    