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


def real_ask_capacity_cushion_policy(ask_counter, min_counter_reinstate, with_reinstate_window, natural_price, upper_target_cushion, ask_capacity_target_cushion, upper_target_wall, ask_capacity_cushion_prior, net_flow, reserves_in, liq_stables_prior, amm_k):
    if (sum(ask_counter) >= min_counter_reinstate or with_reinstate_window == 'No') and natural_price < upper_target_cushion:
        ask_capacity_cushion = ask_capacity_target_cushion
    elif natural_price > upper_target_cushion and natural_price <= upper_target_wall:
        ask_capacity_cushion = upper_target_cushion and ask_capacity_cushion_prior - \
            (net_flow - reserves_in + liq_stables_prior) / \
            upper_target_cushion + \
            (amm_k / upper_target_cushion) ** (1/2) or 0
    else:
        ask_capacity_cushion = ask_capacity_cushion_prior

    if ask_capacity_cushion < 0:
        ask_capacity_cushion = 0
    elif ask_capacity_cushion > ask_capacity_target_cushion:
        ask_capacity_cushion = ask_capacity_target_cushion

    return ask_capacity_cushion


def effective_bid_capacity_cushion_policy(natural_price, lower_target_cushion, lower_target_wall, bid_capacity_cushion_prior, bid_capacity_cushion):
    if natural_price <= lower_target_cushion and natural_price > lower_target_wall:
        bid_change_cushion_usd = bid_capacity_cushion_prior - bid_capacity_cushion
        bid_change_cushion_ohm = lower_target_cushion and (
            bid_capacity_cushion_prior - bid_capacity_cushion) / lower_target_cushion or 0
    else:
        bid_change_cushion_usd = 0
        bid_change_cushion_ohm = 0

    # Ensure that change is smaller than capacity left
    if bid_change_cushion_ohm > bid_capacity_cushion_prior:
        bid_change_cushion_usd = bid_capacity_cushion_prior
        bid_change_cushion_ohm = lower_target_cushion and bid_capacity_cushion_prior / \
            lower_target_cushion or 0

    return bid_change_cushion_usd, bid_change_cushion_ohm
