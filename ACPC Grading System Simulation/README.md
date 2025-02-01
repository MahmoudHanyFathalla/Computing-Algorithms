# ACPC Grading System Simulation
[View Documentation](./ACPC Grading System Simulation/project.pdf)

## Overview
This project simulates the grading process at the Arab Collegiate Programming Contest (ACPC), modeling the arrival and processing of tasks submitted by participants. It provides insights into system performance, including queue lengths, computer utilization, and task completion times.

## Features
- Simulates task arrivals using a Poisson distribution.
- Models service times using an exponential distribution.
- Implements a queue system to manage grading tasks.
- Allocates computing resources efficiently to process submissions.
- Generates visualizations for queue length, computer utilization, and task completion times.

## Installation
To run the simulation, ensure you have Python installed along with the required dependencies:
```bash
pip install numpy matplotlib
```

## Usage
Run the following command to start the simulation:
```bash
python acpc_grading_simulation.py
```
You can modify the parameters inside the script to adjust arrival rates, service times, and the number of grading computers.

## Output
The simulation generates:
- A queue length plot over time.
- A computer utilization graph.
- A histogram of task completion times.

## Customization
You can tweak the following parameters:
- **Arrival rate (lambda)**: Controls how frequently tasks arrive.
- **Service time (mu)**: Defines how long grading takes.
- **Number of computers**: Adjusts the parallel processing capability.

## Future Enhancements
- Implement different queuing strategies (e.g., priority queues).
- Introduce varying service time distributions.
- Optimize task scheduling for better performance.

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements.

## Contact
For any inquiries, please contact [Your Name] at [Your Email].

