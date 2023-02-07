def p_soros_whale(_params, substep, state_history, state) -> dict:
    day = len(state_history)
    out = {}
    if day == _params["soros_short_timing"]:
        out["whale_short"] = _params["soros_short_amount"]
    else:
        out["whale_short"] = 0

    if day == _params["soros_close_out_timing"]:
        out["whale_close_out"] = _params["soros_long_position"]
        # Net out needing to close out the short position
        out["whale_close_out"] -= _params["soros_short_amount"]
    else:
        out["whale_close_out"] = 0

    return out


def s_soros_whale(_params, substep, state_history, state, _input) -> tuple:
    whale_net_flow_amount = - _input["whale_short"] - _input["whale_close_out"]
    whale_net_flow_amount = whale_net_flow_amount * state["price"]
    return ("net_flow", state["net_flow"] + whale_net_flow_amount)


def s_soros_whale_flow(_params, substep, state_history, state, _input) -> tuple:
    return ("whale_flow", _input["whale_short"] + _input["whale_close_out"])


def p_soros_revenue(_params, substep, state_history, state) -> dict:
    # Flow * midpoint of price = revenue
    start_price = state_history[-1][0]["price"]
    end_price = state["price"]
    midpoint_price = (start_price + end_price) / 2
    soros_revenue = midpoint_price * state["whale_flow"]

    return {"soros_revenue": soros_revenue}


def s_soros_revenue(_params, substep, state_history, state, _input) -> tuple:
    return ("soros_revenue", _input["soros_revenue"])


def p_soros_whale_reaction(_params, substep, state_history, state) -> dict:
    return {"whale_reaction": 0}


def s_soros_whale_reaction(_params, substep, state_history, state, _input) -> tuple:
    print(_input["whale_reaction"])
    return ("net_flow", state["net_flow"] + _input["whale_reaction"])
