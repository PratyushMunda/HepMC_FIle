# HEPMC File Analysis

## Overview
This script processes a HEPMC file to analyze particle collision events.It extracts event details, computes transverse momentum distributions for final-state particles, and visualizes the data.

## Features
- Counts the total number of events.
- Number of particles per event.
- Computes the transverse momentum distribution for status=1 particles.
- Basic statistics (mean, max, min pT).
- Plots histograms for:
  - Number of particles per event.
  - Transverse momentum (pT) distribution (with a log-scale option for better visiblility).

## Dependencies
Following Python packages are installed before running the script:
```sh
pip install pyhepmc numpy matplotlib
```

## Usage
1. Update the `path` variable in the script to the correct location of your `.hepmc` file.
2. Run the script:
```sh
python script.py
```
3. Enter the number of final-state particles to display when prompted.
4. The script will:
   - Print the number of events and particles per event.
   - Compute and display pT statistics.
   - Show two histograms for visualization.

## Example Output
```
Total number of events: 1000
Enter number of final-state particles you want to see range from (1-50000): 10
Particle 1: pT = 12.34 GeV/c
Particle 2: pT = 5.67 GeV/c
...
Mean pT: 20.45 GeV/c
Max pT: 150.78 GeV/c
Min pT: 0.01 GeV/c
```

## Visualization
- **Histogram 1:** Distribution of particles per event.
  ![alt text](https://github.com/PratyushMunda/HepMC_FIle/blob/28a60c727f960991bac5273e8ad60fe596e0d38b/Figure_1.png)
- **Histogram 2:** Distribution of transverse momentum (pT) with a logarithmic y-axis for better visibility.
  ![alt text](https://github.com/PratyushMunda/HepMC_FIle/blob/28a60c727f960991bac5273e8ad60fe596e0d38b/Figure_2.png)
  

