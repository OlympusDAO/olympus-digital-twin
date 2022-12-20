def real_bid_capacity_cushion_policy(bid_counter, min_counter_reinstate, with_reinstate_window, natural_price, lower_target_cushion, bid_capacity_target_cushion, bid_capacity_target_cushion_prior, lower_target_wall, net_flow, reserves_in, liq_stables_prior, amm_k, bid_capacity_cushion_prior):

    # Refill capacity
    if (sum(bid_counter) >= min_counter_reinstate or with_reinstate_window == "No") and natural_price > lower_target_cushion:
        bid_capacity_cushion = bid_capacity_target_cushion
    elif natural_price < lower_target_cushion and natural_price >= lower_target_wall:  # Deploy cushion capcity
        bid_capacity_cushion = bid_capacity_target_cushion_prior + \
            net_flow - reserves_in + liq_stables_prior - \
            (amm_k + lower_target_cushion) ** (1/2)

    else:
        bid_capacity_cushion = bid_capacity_cushion_prior

    if bid_capacity_cushion < 0:
        bid_capacity_cushion = 0
    elif bid_capacity_cushion > bid_capacity_target_cushion:
        bid_capacity_cushion = bid_capacity_target_cushion

    return bid_capacity_cushion
