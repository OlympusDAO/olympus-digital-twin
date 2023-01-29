from ..policy.treasury import treasury_liquidity_policy, treasury_reserves_policy, treasury_liq_safety_check


def p_treasury(params, substep, state_history, state) -> dict:
    day = len(state_history)
    prev_day = state_history[-1][-1]
    liq_stables_prior = prev_day["liq_stables"]
    net_flow = state["net_flow"]
    net_flow_bondsale = state['netflow_bondsale']
    net_flow_bondexpire = state['netflow_bondexpire']
    reserves_in = state["reserves_in"]
    bid_change_usd = state["bid_change_usd"]
    ask_change_usd = state["ask_change_usd"]
    amm_k = state["amm_k"]
    reserves_stables_prior = prev_day["reserves_stables"]
    price_prior = prev_day["price"]
    cum_ohm_purchased_prior = prev_day["cum_ohm_purchased"]
    cum_ohm_burnt_prior = prev_day["cum_ohm_burnt"]
    cum_ohm_minted_prior = prev_day["cum_ohm_minted"]
    bid_change_ohm = state["bid_change_ohm"]
    ask_change_ohm = state["ask_change_ohm"]

    #liq_safety_check = treasury_liq_safety_check(liq_stables_prior,net_flow_bondexpire,params['liq_stables_safety_ratio'],day)

    liq_stables, liq_ohm, price = treasury_liquidity_policy(
        liq_stables_prior, net_flow, net_flow_bondsale, net_flow_bondexpire, reserves_in, bid_change_usd, ask_change_usd, amm_k,day)

    reserves_out, reserves_stables, ohm_traded, cum_ohm_purchased, cum_ohm_burnt, cum_ohm_minted = treasury_reserves_policy(liq_stables, liq_stables_prior, net_flow, net_flow_bondsale, net_flow_bondexpire, reserves_stables_prior,
                                                                                                                            price, price_prior, cum_ohm_purchased_prior, cum_ohm_burnt_prior, cum_ohm_minted_prior, bid_change_ohm, ask_change_ohm)
    return {"liq_stables": liq_stables,
            "liq_ohm": liq_ohm,
            "price": price, "reserves_out": reserves_out, "reserves_stables": reserves_stables,
            "ohm_traded": ohm_traded, "cum_ohm_purchased": cum_ohm_purchased, "cum_ohm_burnt": cum_ohm_burnt, "cum_ohm_minted": cum_ohm_minted}


def s_liq_stables(_params, substep, state_history, state, _input) -> tuple:
    return ("liq_stables", _input["liq_stables"])


def s_liq_ohm(_params, substep, state_history, state, _input) -> tuple:
    return ("liq_ohm", _input["liq_ohm"])


def s_price(_params, substep, state_history, state, _input) -> tuple:
    assert _input["price"] > 0, "price should be bigger than 0"
    return ("price", _input["price"])


def s_reserves_out(_params, substep, state_history, state, _input) -> tuple:
    return ("reserves_out", _input["reserves_out"])


def s_reserves_stables(_params, substep, state_history, state, _input) -> tuple:
    return ("reserves_stables", _input["reserves_stables"])


def s_ohm_traded(_params, substep, state_history, state, _input) -> tuple:
    return ("ohm_traded", _input["ohm_traded"])


def s_cum_ohm_purchased(_params, substep, state_history, state, _input) -> tuple:
    return ("cum_ohm_purchased", _input["cum_ohm_purchased"])


def s_cum_ohm_burnt(_params, substep, state_history, state, _input) -> tuple:
    return ("cum_ohm_burnt", _input["cum_ohm_burnt"])


def s_cum_ohm_minted(_params, substep, state_history, state, _input) -> tuple:
    return ("cum_ohm_minted", _input["cum_ohm_minted"])
