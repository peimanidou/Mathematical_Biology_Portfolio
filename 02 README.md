# 02 — Exponential Growth Model

## Description
**Exponential Growth Model** for tumor cell dynamics using Python.

In the early stages of tumor development,both nutrients 
and space are assumed to be unlimited. Under these 
conditions, tumor cells grow exponentially 
without resource limitations.

## Biological Context
As described by R. P. Araujo and D. L. S. McElwain:
*"When the entire tissue volume was growing, 
exponential growth was expected, with the growth 
rate gradually reducing as the region of active 
growth was progressively restricted to an outer 
shell of tissue."*


**Note:** The parameters do not follow real values and are used 
purely for this specific modeling

## The Model
The exponential growth ODE:

dP/dt = r * P 

Where:
- P : population size (tumor cells)
- r : proliferation rate of tumor cells (1/unit time)

## Parameters Used
| Parameter | Value | Description |
|-----------|-------|-------------|
| P₀ | 4 | Initial population of tumor cells |
| r | 0.2 | Proliferation rate |

## Tools
- Python 3
- NumPy
- SciPy (odeint)
- Matplotlib

  ## Output
![Exponential Growth Model](02%20Exponential%20Growth.png)

## Part of
Mathematical Biology Portfolio 
