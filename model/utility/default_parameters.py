from model.policy.ohmbond import generate_ohmbond

default_params1 = {"demand_factor": [.07],
                   "supply_factor": [-.07],
                   "initial_reserves_volatile": [25000000],
                   # LiquidityUSD : reservesUSD ratio --> 1:1 = 0.5
                   "max_liq_ratio": [0.14375],
                   "target_ma": [30],  # number of days
                   "lower_wall": [0.15],
                   "upper_wall": [0.15],
                   "lower_cushion": [.075],
                   "upper_cushion": [.075],
                   "reinstate_window": [30],
                   "max_outflow_rate": [0.05],
                   "reward_rate_policy": ["Flat"],
                   # % of floating supply that the treasury can deploy when price is trading above the upper target
                   "ask_factor": [0.095],
                   # % of the reserves that the treasury can deploy when price is trading below the lower target
                   "bid_factor": [0.095],
                   # The percentage of a bid or ask to offer as a cushion
                   "cushion_factor": [0.3075],
                   # Number of days within the reinstate window that conditions are true to reinstate a bid or ask
                   "min_counter_reinstate": [6],
                   "with_reinstate_window": ['Yes'],
                   "bond_create_schedule": [generate_ohmbond(amounts=[[1e6]*3], exp_durs=[[30, 60, 90]])],
                   "bond_annual_discount_rate": [.04],
                   "ohm_bond_to_netflow_ratio":[0.5] #should be between 0 and 1
                   }
