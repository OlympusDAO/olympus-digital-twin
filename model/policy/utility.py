def p_list_params(params, substep, state_history, state) -> dict:
    # Function to pull out any parameters that should be recorded

    # Meant to ensure only relevant parameters are taken out and not overloading the dataframe size

    return {"demand_factor": params["demand_factor"],
            "supply_factor": params["supply_factor"],
            "bond_annual_discount_rate": params["bond_annual_discount_rate"]}
