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