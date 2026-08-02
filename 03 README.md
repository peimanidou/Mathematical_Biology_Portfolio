# 03 — Gompertz Growth Model

## Description
**Gompertz Growth Model** for tumor's volume growth using Python.

## Biology Background

One of the best known tumor growth model, originated in 1825 the Gompertz 
has been shown to provide excellent fits to pre-clinical and clinical tumor growth data.
It is visualised as an S-shaped (sigmoidal curve) where the inflection point occurs once 37% of the maximum tumor volume 
has been reached

## Reference
Heesterman, B.L. et al. (2019). 
"Mathematical Models for Tumor Growth and the Reduction of Overtreatment."
Journal of Neurological Surgery B: Skull Base.
DOI: 10.1055/s-0038-1667148

**Note:** The parameters do not follow real values and are used 
purely for this specific modeling

## The Model
The Gompertz growth ODE:

dV/dt = r * V * ln (K/V) 

Where:
- V : tumor's volume
- r : growth rate
- K : carrying capacity of given environment

## Parameters Used
| Parameter | Value | Description |
|-----------|-------|-------------|
| V₀ | 0.5 | Initial volume of the tumor with unit x^3 |
| r | 0.01 | Growth rate |
| K | 10,000 | Carrying capacity of the environment |

## Tools
- Python 3
- NumPy
- SciPy (odeint)
- Matplotlib

  ## Output
![Gompertz Growth Model](03%20Gompertz%20Growth.png)

## Part of
Mathematical Biology Portfolio 
