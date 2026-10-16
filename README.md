# Modeling and Simulation of a Bank Queue System

A Python-based bank queue simulation that models customer arrivals, teller availability, and service durations to analyze customer waiting times and banking service efficiency.

## Overview

The **Bank Queue System Simulation** is an academic project developed to analyze how customer volume, service times, and the number of available tellers affect queue performance in a bank.

Using the **Monte Carlo method** and probability-based modeling, the system simulates customer arrivals and teller service allocation. It processes a CSV dataset representing 30 days of simulated banking operations and calculates key performance metrics to help evaluate service efficiency.

The project also includes an interactive **Bank Manager Scenario Page**, allowing users to experiment with different customer volumes and teller configurations and observe their effects on waiting times.

## Features

- **30-Day Queue Simulation** – Processes simulated banking activity stored in a CSV file.
- **Customer Arrival Modeling** – Represents customer arrival intervals using probability-based distributions.
- **Teller Allocation** – Assigns customers to available tellers based on arrival time and teller availability.
- **Waiting Time Analysis** – Calculates average and maximum customer waiting times.
- **Interactive Scenario Simulation** – Allows users to adjust the number of customers and available tellers.
- **Performance Comparison** – Demonstrates how different teller configurations affect waiting times.
- **Tabular Results** – Displays simulation records and results for analysis.
- **Banking Schedule Modeling** – Represents banking hours from 9:00 AM–12:00 PM and 1:00 PM–4:30 PM, with a lunch break from 12:00 PM–1:00 PM.

## Technologies Used

- **Python** – Simulation logic and calculations
- **HTML** – Web page structure
- **CSS** – Styling and layout
- **JavaScript** – Interactive web interface
- **CSV** – Input dataset for customer arrivals and service times

## Simulation Methodology

The system uses probability-based modeling and the Monte Carlo method to simulate a multi-teller banking environment.

### Input Data

The CSV dataset represents 30 days of simulated bank activity and includes the following fields:

| Field | Description |
|---|---|
| `day` | Simulation day |
| `tellers` | Number of available tellers |
| `customer_id` | Customer identifier |
| `arrival_time` | Customer inter-arrival time |
| `service_time` | Customer service duration |
| `arrival_clock` | Cumulative customer arrival time |

### Simulation Process

1. Load customer and teller information from the CSV dataset.
2. Determine customer arrival times.
3. Track teller availability and assign customers when a teller becomes available.
4. Calculate each customer's waiting time.
5. Compute average and maximum waiting times after processing the simulation.
6. Display the results for analysis.

### Performance Metrics

- **Average Waiting Time** – The mean time customers spend waiting before service begins.
- **Maximum Waiting Time** – The longest waiting time experienced by any customer.

The results are presented in minutes and seconds for easier interpretation.

## Bank Manager Scenario Page

The interactive scenario page allows users to specify:

- The number of customers entering the bank.
- The number of tellers available to serve them.

The simulation then displays the resulting average and maximum waiting times.

In the project's test scenarios, increasing teller availability generally reduced customer waiting times, while high customer volumes with fewer tellers resulted in longer queues.

## Banking Schedule

The simulation represents the following operating hours:

| Schedule | Time |
|---|---|
| Morning operations | 9:00 AM – 12:00 PM |
| Lunch break | 12:00 PM – 1:00 PM |
| Afternoon operations | 1:00 PM – 4:30 PM |

The dataset incorporates variations in customer volume, arrival intervals, service durations, and teller availability to represent different banking scenarios.

## Project Objectives

- Analyze customer waiting times in a multi-teller banking system.
- Evaluate the effects of customer volume and teller availability.
- Identify configurations that may improve service efficiency.
- Support data-driven decisions about teller allocation and queue management.
- Demonstrate how simulation can be used to study real-world service systems.

## Potential Improvements

Future enhancements could include:

- Customer priority levels and different transaction types.
- Multiple queues and customer abandonment.
- More detailed variations in teller efficiency.
- Appointment and digital queue management systems.
- Updated datasets based on actual bank transaction records.
- Additional performance metrics, such as queue length and teller utilization.

## References

1. Choudhury, Nahar, & Pritom (2023). *Service Time Reduction Through the Development of a Simulation Model in a Selected Bank.* [Read paper](https://doi.org/10.51983/ajms-2023.12.1.3488)
2. Jamil, Mobin, & Bhowmik (2023). *Improving Service Quality of a Banking System Through Discrete-Event Simulation.* [Read paper](https://ieomsociety.org/proceedings/2023dhaka/79.pdf)
3. Yifter et al. (2023). *Simulation-Based Optimization of a Bank Queuing System: Evidence from the Commercial Bank of Ethiopia.* [Read paper](https://www.tandfonline.com/doi/full/10.1080/23311916.2023.2274522)
4. SimPy Documentation. *The Bank Tutorial – Modeling a Bank Queuing System Using Python SimPy.* [Read tutorial](https://pythonhosted.org/SimPy/Tutorials/TheBank.html)

---
