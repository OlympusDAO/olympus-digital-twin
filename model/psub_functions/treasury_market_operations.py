def p_real_bid_capacity_cushion(_params, substep, state_history, state) -> dict:
    prev_day = state_history[-1][-1]
    if (sum(state["bid_counter"]) >= _params["min_counter_reinstate"] or _params["with_reinstate_window"] == "No") and state["natural_price"] > state["lower_target_cushion"]:  # Refill capacity
        ask_capacity_cushion = state["bid_capacity_target_cushion"]
    elif state["natural_price"] < state["lower_target_cushion"] and state["natural_price"] >= state["lower_target_wall"]:  # Deploy cushion capcity
        ask_capacity_cushion =

                self.bid_capacity_cushion = prev_day.bid_capacity_cushion + self.net_flow - \
                    self.reserves_in + prev_day.liq_stables - \
                        (self.k * self.lower_target_cushion) ** (1/2)
            else:
                self.bid_capacity_cushion = prev_day.bid_capacity_cushion
            
            if self.bid_capacity_cushion < 0:
                self.bid_capacity_cushion = 0
            elif self.bid_capacity_cushion > self.bid_capacity_target_cushion:
                self.bid_capacity_cushion = self.bid_capacity_target_cushion


def p_real_ask_capacity_cushion(_params, substep, state_history, state) -> dict:
    if (sum(self.ask_counter) >= params.min_counter_reinstate or params.with_reinstate_window == 'No') and natural_price < self.upper_target_cushion:
                self.ask_capacity_cushion = self.ask_capacity_target_cushion
            elif natural_price > self.upper_target_cushion and natural_price <= self.upper_target_wall:
                self.ask_capacity_cushion = self.upper_target_cushion and prev_day.ask_capacity_cushion - (self.net_flow - self.reserves_in + prev_day.liq_stables) / self.upper_target_cushion + (self.k / self.upper_target_cushion) ** (1/2) or 0
            else:
                self.ask_capacity_cushion = prev_day.ask_capacity_cushion

            if self.ask_capacity_cushion < 0:
                self.ask_capacity_cushion = 0
            elif self.ask_capacity_cushion > self.ask_capacity_target_cushion:
                self.ask_capacity_cushion = self.ask_capacity_target_cushion


def s_bid_capacity_cushion(_params, substep, state_history, state, _input) -> tuple:
    return ("bid_capacity_cushion", _input["bid_capacity_cushion"])


def s_ask_capacity_cushion(_params, substep, state_history, state, _input) -> tuple:
    return ("ask_capacity_cushion", _input["ask_capacity_cushion"])
