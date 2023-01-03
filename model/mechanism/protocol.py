    
def floating_supply_mechanism(supply,liq_ohm):
    return max(supply-liq_ohm,0)
def mcap_mechanism(supply,price):
    return supply * price
def ratio_mechanism(r1,r2):
    return (r2 and r1/r2)