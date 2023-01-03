def p_reserves_in(params, substep, state_history, state) -> dict:
    day = len(state_history)
    prior_day = state_history[-1][-1]

    if day % 7 == 0:  # Rebalance once a week
        reserves_in = prior_day["liq_stables"] - \
            prior_day["treasury_stables"] * params["max_liq_ratio"]
        if prior_day["target_liq_ratio_reached"] is False:
            # Smaller max_outflow_rate until target is first reached
            max_outflow = (-1) * prior_day["reserves_stables"] * \
                params["max_outflow_rate"] * 2 / 3
        else:
            # Ensure that the reserve release is limited by max_outflow_rate
            max_outflow = (-1) * prior_day["reserves_stables"] * \
                params["max_outflow_rate"]

        if reserves_in < max_outflow:
            reserves_in = max_outflow
        # Ensure that the reserve release is limited by the total reserves left
        if reserves_in < (-1) * prior_day["reserves_stables"]:
            reserves_in = (-1) * prior_day["reserves_stables"]
    else:
        reserves_in = 0
    return {'reserves_in': reserves_in}


def treasury_liquidity_policy(liq_stables_prior, net_flow, reserves_in, bid_change_usd, ask_change_usd, amm_k):
    liq_stables = max(liq_stables_prior + net_flow -
                      reserves_in + bid_change_usd - ask_change_usd, 0)
    # ensure that if liq_stables is 0 then liq_ohm is 0 as well
    liq_ohm = liq_stables and amm_k / liq_stables or 0
    # ensure that if liq_ohm is 0 then price is 0 as well
    price = liq_ohm and liq_stables / liq_ohm or 0

    return liq_stables, liq_ohm, price


def treasury_reserves_policy(liq_stables, liq_stables_prior, net_flow, reserves_stables_prior,
                             price, price_prior, cum_ohm_purchased_prior, cum_ohm_burnt_prior, cum_ohm_minted_prior, bid_change_ohm, ask_change_ohm):
    reserves_out = liq_stables - liq_stables_prior - \
        net_flow
    reserves_stables = max(reserves_stables_prior - reserves_out, 0)

    ohm_traded = (price + price_prior) and (-2) * \
        reserves_out / (price + price_prior) or 0
    cum_ohm_purchased = cum_ohm_purchased_prior - ohm_traded
    cum_ohm_burnt = cum_ohm_burnt_prior + bid_change_ohm
    cum_ohm_minted = cum_ohm_minted_prior + ask_change_ohm

    return reserves_out, reserves_stables, ohm_traded, cum_ohm_purchased, cum_ohm_burnt, cum_ohm_minted
