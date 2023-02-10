# Olympus cadCAD Model


## Executive Summary

This repository holds the cadCAD model created by BlockScience for Olympus DAO. It can be used to test a wide variety of simulations and scenarios. 

## What is cadCAD
## Installing cadCAD for running this repo

### 1. Pre-installation Virtual Environments with [`venv`](https://docs.python.org/3/library/venv.html) (Optional):
It's a good package managing practice to create an easy to use virtual environment to install cadCAD. You can use the built in `venv` package.

***Create** a virtual environment:*
```bash
$ python3 -m venv ~/cadcad
```

***Activate** an existing virtual environment:*
```bash
$ source ~/cadcad/bin/activate
(cadcad) $
```

***Deactivate** virtual environment:*
```bash
(cadcad) $ deactivate
$
```

### 2. Installation: 
Requires [>= Python 3.6](https://www.python.org/downloads/) 

**Install Using [pip](https://pypi.org/project/cadCAD/)** 
```bash
$ pip3 install cadcad==0.4.28
```

**Install all packages with requirement.txt**
```bash
$ pip3 install -r requirements.txt
```

## Running a Example

You can see a simple example of how to use the model with just one set of parameters in "Single Example.ipynb".

You can see an example of how to run parameter sweeps in "Sweep Example.ipynb"

## Model Details
### Parameters
#### Market Behavior
`demand_factor`: range (0,+inf), marking how much random demand will be at each time step
`supply_factor`: range (-inf,0), marking how much supply demand will be at each time step

`panic_sell_on`: True or False. If panic sell is going to happen.
`panic_param`: Range (0,+inf). Bigger the larger panic sell amount.

#### Treasury State
`initial_reserves_volatile`: range [0,+inf]. The reserve has two parts, stable and volatile and this markes the value of the latter. Not interacting in the current model.

#### Policy Parameters (non-RBS)
`max_liq_ratio`: range(0,1), marking the ideal ratio of liquidity_stables / treasury_stables. Every 7 days the treasury will take actions according to whether this ratio is reached (detailed in `model.policy.treasury.p_reserves_in`)
`max_outflow_rate`: ranging (0,1), marking the max reserve outflow ratio for the 7-day liq_ratio adjustment behavior
`reward_rate_policy`: default Flat". Does the protocol change their reward rate for staking, which impacts the supply.


#### RBS Parameters
`target_ma`: number of days for moving average price target
`lower_wall`: range [0,1]. Ratio of the lower wall price to the target price.
`upper_wall`: range [0,1]. Ratio of the upper wall price to the target price.
`lower_cushion`: range [0,lower_wall). Ratio of the lower cusion price to the target price.
`upper_cushion`: range [0,upper_wall). Ratio of the upper cushion price to the target price.

`reinstate_window`: range [0,+inf). How many days before the capacity get refilled.
`ask_factor`: range [0,+inf). Ratio of the reserves that the treasury can deploy when price is trading above the target
`bid_factor`: range [0,+inf). Ratio of the reserves that the treasury can deploy when price is trading below the target
`cushion_factor`: ranging [0,+inf). The percentage of a bid or ask to offer as a cushion
`min_counter_reinstate`: range [0,reinstate_window]. Number of days within the reinstate window that conditions are true to reinstate a bid or ask
`with_reinstate_window`: default 'Yes'.


#### OHM Bond Parameters
`bond_create_schedule`: a list of all ohm bonds.
`bond_schedule_name`: name of each bond schedule.
`bond_annual_discount_rate`: range (0,1)
`ohm_bond_to_netflow_ratio`: range (0,1)
