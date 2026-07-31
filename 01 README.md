# 01 — Logistic Growth Model

## Description
**Logistic Growth Model** for bacterial population dynamics using Python.

**Note:** The parameters do not follow real values and are used 
purely for this specific modeling

## The Model
The logistic growth ODE:

dP/dt = r * P * (1 - P/K)

Where:
- P : population size (bacteria)
- r : growth rate
- K : carrying capacity of given environment

## Parameters Used
| Parameter | Value | Description |
|-----------|-------|-------------|
| P₀ | 2 | Initial population of the bacteria |
| r | 0.1 | Growth rate |
| K | 10,000 | Carrying capacity of the environment |

## Tools
- Python 3
- NumPy
- SciPy (odeint)
- Matplotlib

## Part of
Mathematical Biology Portfolio →
pathway to Mathematical Oncology
