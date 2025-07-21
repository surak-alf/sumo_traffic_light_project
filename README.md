# SUMO Traffic Light Simulation Project 🚦🚗

A complete simulation of a signalized intersection using SUMO (Simulation of Urban MObility), demonstrating traffic flow optimization with configurable traffic light timing.

![Simulation Demo](images/sumo.gif) 

# Project Structure 📂

This section outlines the directory and file organization of the `sumo_traffic_light_project`.

* **sumo_traffic_light_project/**
    * **config/**
        * `traffic_lights.tll.xml` # Traffic timing definitions
    * **networks/**
        * `intersection.net.xml` # Generated network file
        * `intersection.nod.xml` # Node definitions
        * `intersection.edg.xml` # Edge definitions
        * `intersection.con.xml` # Connection definitions
        * `network.netcfg.xml` # Network configuration
    * **routes/**
        * `vehicles.rou.xml` # Vehicle routes and flows
    * **simulations/**
        * `simulation.sumocfg` # Main simulation config
        * **output/** # Simulation outputs
            * `tripinfo.xml`
            * `summary.xml`
            * **images/** # Visualization assets
                * `simulation.gif`
    * **analysis/**
        * `compare.py` # Analysis script (optional)


## Prerequisites 🛠️

- [SUMO](https://www.eclipse.org/sumo/) (Version 1.15.0 or newer)
- Python 3.8+ (for analysis scripts)
- Recommended VSCode extensions:
  - XML Tools
  - Python

## Setup & Installation ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/surak-alf/sumo_traffic_light_project.git
   cd sumo_traffic_light_project

2. **Generate the network**:
   ```bash
   netconvert -c networks/network.netcfg.xml

3. **Run the simulation**:
   ```bash
   sumo-gui -c simulations/simulation.sumocfg   

 Key Features ✨
🚥 Configurable 4-way signalized intersection

⏱️ Adjustable traffic light timing plans

📊 Built-in traffic flow analysis

📈 Comparative simulation capability (with/without traffic lights)  

# Traffic Simulation Analysis

## Simulation Scenarios and Results

The following table summarizes the key performance indicators for each simulated scenario:

| Scenario        | Avg Travel Time | Median Travel Time | Avg Waiting Time | Max Waiting Time | Avg Speed     | Vehicles per Hour | Route Efficiency |
| :-------------- | :-------------- | :----------------- | :--------------- | :--------------- | :------------ | :---------------- | :--------------- |
| Base Case       | 23.70           | 21                 | 9.32             | 34               | 5.31          | 1204.01           | 0.382            |
| Optimized Lights | 23.76           | 19                 | 9.45             | 46               | 5.47          | 1197.99           | 0.394            |
| No Traffic Lights | 27.23           | 21.5               | 13.10            | 46               | 5.23          | 1195.99           | 0.377            |

**Note:** Values have been rounded for better readability in the Markdown table. The original precise values are available in the source data.

## Key Observations 

* **Average Travel Time:** The "Base Case" and "Optimized Lights" scenarios show very similar average travel times, with "No Traffic Lights" resulting in a significantly higher average travel time.
* **Median Travel Time:** "Optimized Lights" has the lowest median travel time, suggesting a potentially smoother experience for the majority of vehicles compared to the other two scenarios.
* **Average Waiting Time:** "Base Case" has the lowest average waiting time, while "No Traffic Lights" has the highest.
* **Max Waiting Time:** "Optimized Lights" and "No Traffic Lights" both show a higher maximum waiting time compared to the "Base Case."
* **Average Speed:** "Optimized Lights" achieves the highest average speed, indicating more efficient movement of vehicles.
* **Vehicles per Hour:** All scenarios show a relatively similar number of vehicles processed per hour.
* **Route Efficiency:** "Optimized Lights" demonstrates the highest route efficiency, suggesting better utilization of the road network.

## Conclusion 

Based on these simulation results, the **"Optimized Lights"** scenario appears to offer the best overall performance, demonstrating improvements in median travel time, average speed, and route efficiency, despite a slightly higher maximum waiting time. The **"No Traffic Lights"** scenario, surprisingly, performs worse in terms of average travel time and average waiting time, indicating that traffic lights, when properly optimized, are crucial for managing traffic flow in this simulated environment.