def p_soros_whale(_params, substep, state_history, state) -> dict:
    day = len(state_history)
    out = {}
    if day == _params["soros_short_timing"]:
        out["whale_short"] = _params["soros_short_amount"]
    else:
        out["whale_short"] = 0
    return out


def s_soros_whale(_params, substep, state_history, state, _input) -> tuple:
    return ("net_flow", state["net_flow"] - _input["whale_short"])


def s_soros_whale_flow(_params, substep, state_history, state, _input) -> tuple:
    return ("whale_flow", _input["whale_short"])
