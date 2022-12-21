from ..policy.treasury import treasury_liquidity_policy


def p_treasury(params, substep, state_history, state) -> dict:
    prev_day = state_history[-1][-1]
    liq_stables_prior = prev_day["liq_stables"]
    net_flow = state["net_flow"]
    reserves_in = state["reserves_in"]
    bid_change_usd = state["bid_change_usd"]
    ask_change_usd = state["ask_change_usd"]
    amm_k = state["amm_k"]
    liq_stables, liq_ohm, price = treasury_liquidity_policy(
        liq_stables_prior, net_flow, reserves_in, bid_change_usd, ask_change_usd, amm_k)
    return {"liq_stables": liq_stables,
            "liq_ohm": liq_ohm,
            "price": price}


def s_liq_stables(_params, substep, state_history, state, _input) -> tuple:
    return ("liq_stables", _input["liq_stables"])


def s_liq_ohm(_params, substep, state_history, state, _input) -> tuple:
    return ("liq_ohm", _input["liq_ohm"])


def s_price(_params, substep, state_history, state, _input) -> tuple:
    assert _input["price"] > 0
    return ("price", _input["price"])
