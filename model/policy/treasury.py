def p_reserves_in(params, substep, state_history, state) -> dict:
    day = len(state_history)  # note: not sure if this is the right way!!

    if day % 7 == 0:  # Rebalance once a week
        reserves_in = state["liq_stables"] - \
            state["treasury_stables"] * params["max_liq_ratio"]
        if state["target_liq_ratio_reached"] is False:
            # Smaller max_outflow_rate until target is first reached
            max_outflow = (-1) * state["reserves_stables"] * \
                params["max_outflow_rate"] * 2 / 3
        else:
            # Ensure that the reserve release is limited by max_outflow_rate
            max_outflow = (-1) * state["reserves_stables"] * \
                params["max_outflow_rate"]

        if reserves_in < max_outflow:
            reserves_in = max_outflow
        # Ensure that the reserve release is limited by the total reserves left
        if reserves_in < (-1) * state["reserves_stables"]:
            reserves_in = (-1) * state["reserves_stables"]
    else:
        reserves_in = 0
    return {'reserves_in': reserves_in}
