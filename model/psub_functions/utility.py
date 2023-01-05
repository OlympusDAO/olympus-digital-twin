def s_list_params(variable):
    # Factory which creates state update step

    def output_function(_params, substep, state_history, state, _input):
        return (variable, _input[variable])

    return output_function
