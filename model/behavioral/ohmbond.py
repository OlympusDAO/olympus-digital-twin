import numpy as np
def price_curve(expiration_duration:int,discount_factor = 1/5)->float:
    # given the duration, return a discount rate (should be between (0,1) for rational decision-makers...)
    # longer the duration is, bigger discount it should be
    # discount factor shoudl be smaller than 1, bigger than 0. bigger discount factor, more temporal discount (meaning the longer expiration duration bonds will be cheaper)
    # future to-do: 1) find better estimates or allow flexible change of the assumption
    assert discount_factor < 1
    discounted_price = 1/(expiration_duration/28)**discount_factor # 28 assuming for a 30 day bond the discount rate is close to 1
    discounted_price = max(1,discounted_price + np.random.randn()*.01)
    return discounted_price

def bond_sell_batch_auction(bonds:list):
    total_sell_amount = 0
    for bond in bonds:
        av_price = price_curve(bond.expiration_duration)
        sell_amount = bond.total_amount*av_price
        total_sell_amount += sell_amount
    return total_sell_amount
    