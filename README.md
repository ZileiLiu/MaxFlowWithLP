# Solving Max-flow with linear programming

## Overview
This project demonstrates a Max Flow Solver using Linear Programming (LP) and the Simplex algorithm. It includes utilities to create linear programming matrices from flow network data, a simplex solver to optimize flow, and functions to handle matrix visualization. The code allows users to define networks, convert them into LP form, and solve for the maximum flow efficiently.

## Features
- Matrix Conversion for LP: Generates matrices for LP formulations based on given network flow data.
- Simplex Solver: Implements a simplex method to find the optimal solution to maximize flow within defined network constraints.
- Flexible Network Input: Supports different network configurations as inputs, providing flexibility in defining nodes, edges, and capacities.

## Project Structure
### Code:
- MaxFlowModelling.py: Contains create_lp_matrices, which translates the network data into LP format.
- LpSolverSimplex.py: Provides a simplex solver to maximize flow, solving the LP generated for each network.
- main.py: Initializes sample networks and demonstrates solving the max flow for different configurations.
### Documentation:
- MaxFlow_Report.pdf: Detailed report on the LP model for max flow, matrix construction, Simplex algorithm, and sample outputs.

## Usage
- Open a terminal in the project directory and execute: python3 main.py
- The code will output the solution matrix showing flow values between nodes, and display the objective value representing the maximum flow.
- View the Report: For a thorough understanding of the LP formulation, Simplex solver, and example networks, refer to the report here.

## Requirements
Python 3.8+

## Contact
For any questions or suggestions, please contact zilei.james.liu@gmail.com 
