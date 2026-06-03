# pbh-memory-burden-constraints

This repository contains numerical codes for cosmological constraints on evaporating primordial black holes (PBHs) with the **memory burden effect**, based on:

- **Primary reference**: Montefalcone et al. (2025), arXiv:2503.21005 [astro-ph.CO], *"Does Memory Burden Open a New Mass Window for PBHs as Dark Matter?"* — later updated to *"Can a Breakdown of Hawking Evaporation Open a New Mass Window for Primordial Black Holes as Dark Matter?"*, *Phys. Rev. D* **113**, 023524 (2026)
- **This work**: Zhang, Yang, and Jin (2025), *"Phenomenologically Modeling the Continuous Crossover of Primordial Black Holes under Memory-Burden Effect"* (in preparation)

## Key Results

| Task | Status |
|:---|:---|
| BBN constraint via decaying-particle mapping | :white_check_mark: |
| CMB + BBN combined constraints (Fig. 3) | :white_check_mark: |
| Four transition functions validation | :white_check_mark: |

## Python Scripts

| File | Description |
|:---|:---|
| `pbh_bbn_v2.py` | BBN constraint via decaying-particle mapping (Keith+2020, Kawasaki+2018) |
| `pbh_cmb_fixed.py` | CMB constraint via three-phase independent calculation (Acharya+2019) |
| `pbh_combined.py` | Merges CMB + BBN constraints; reproduces Fig. 3 of Montefalcone+2025 |
| `pbh_four_transitions.py` | Validates 4 smooth transition functions (h1-h4) under additive/multiplicative distributions |

## Jupyter Notebook

[pbh_memory_burden_CN.ipynb](pbh_memory_burden_CN.ipynb) — contains all 6 result figures (base64 embedded); no additional downloads required.

## Requirements

```bash
pip install numpy scipy matplotlib
```

## Quick Start

```bash
# Generate CMB constraints
python pbh_cmb_fixed.py

# Generate BBN constraints
python pbh_bbn_v2.py

# Generate combined CMB+BBN constraints (reproduces Fig. 3)
python pbh_combined.py

# Validate four transition functions
python pbh_four_transitions.py
```

## Physical Methods

- **BBN**: Decaying-particle mapping (Keith+2020, Kawasaki+2018)
- **CMB**: Three-phase independent calculation (Acharya+2019)
- **Combined**: f_combined = min(f_CMB, f_BBN)

### Key Parameters

| Parameter | Description | Typical Values |
|:---|:---|:---|
| `q` | Transition mass fraction (M_trans = q * M_i) | 0.2, 0.5, 0.8 |
| `delta` | Transition width (smoothness); delta=0 = step-like | 0, 0.1, 0.3 |
| `k` | Memory-burden power-law exponent | 2 |

## Output Figures

Running the scripts produces the following figures:

| Figure | Description |
|:---|:---|
| `pbh_cmb_fixed.png` | CMB constraints for different (q, delta) parameters |
| `bbn_constraint_plot.png` | BBN constraints for different (q, delta) parameters |
| `fig3_reproduction.png` | Combined CMB+BBN constraints (reproduces Fig. 3) |
| `delta_scan.png` | Parameter scan varying delta (fixed q=0.5) |
| `q_scan.png` | Parameter scan varying q (fixed delta=0.1) |
| `four_transitions_comparison.png` | Comparison of 4 transition functions x 2 distributions |
| `abundance_enhancement.png` | Enhancement ratio f_new / f_default |

## References

- Acharya & Khatri (2020), *JCAP* **06**, 018, arXiv:2002.00898
- Kawasaki et al. (2018), *Phys. Rev. D* **97**, 023502
- Keith et al. (2020), *Phys. Rev. D* **102**, 103512
- Montefalcone et al. (2025/2026), arXiv:2503.21005 [astro-ph.CO], *Phys. Rev. D* **113**, 023524
