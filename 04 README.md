# 04 — von Bertalanffy-Pütter Tumor Growth Model

## Description
**von Bertalanffy-Pütter Growth Model** for tumor volume dynamics using Python.

This model incorporates the metabolic balance between nutrient inflow for cellular proliferation and energy consumption for cellular maintenance and cell death.

**Note:** The parameters used in this simulation serve illustrative purposes to demonstrate the growth behavior toward carrying capacity.

## Biology & Mathematical Background
The von Bertalanffy-Pütter growth equation models tumor dynamics as a balance between two competing biological processes:
1. **Anabolism / Proliferation ($p \cdot V^a$):** Nutrient and energy inflow proportional to the tumor surface area ($a = 2/3$).
2. **Catabolism / Cell Loss ($q \cdot V^b$):** Energy required for maintenance and cell death proportional to total tumor volume ($b = 1$).

As tumor volume increases, catabolic loss eventually balances anabolic growth, reaching a theoretical carrying capacity:
$$K = \left(\frac{p}{q}\right)^{\frac{1}{b-a}}$$

## The Model
The von Bertalanffy-Pütter ODE:

dV/dt = p * V^a - q * V^b

Where:
- V : tumor volume (mm³)
- p : proliferation rate coefficient
- q : cell death rate coefficient
- a : surface scaling exponent (2/3 for 3D tumor geometry)
- b : volume scaling exponent (1)

## Parameters Used
| Parameter | Value | Description |
|-----------|-------|-------------|
| V₀ | 225 | Initial tumor volume (mm³) |
| p | 0.1 | Proliferation rate coefficient |
| q | 0.01 | Cell loss / death rate coefficient |
| a | 2/3 | Surface area scaling exponent |
| b | 1.0 | Volume scaling exponent |

## Output
![von Bertalanffy Tumor Growth Model](04_von_Bertalanffy_model.png)

## Tools
- Python 3
- NumPy
- SciPy (odeint)
- Matplotlib

## Reference
- Kühleitner, M., Brunner, N., Nowak, W.G., Renner-Martin, K., & Scheicher, K. (2019). 
  "Best fitting tumor growth models of the von Bertalanffy-Pütter Type." 
  *BMC Cancer*, 19:683. 
  DOI: [10.1186/s12885-019-5911-y](https://doi.org/10.1186/s12885-019-5911-y) | PMCID: PMC6624893

## Part of
Mathematical Biology Portfolio 
