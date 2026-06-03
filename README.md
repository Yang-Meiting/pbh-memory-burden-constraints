# pbh-memory-burden-constraints

Numerical tools for cosmological constraints on evaporating primordial black holes (PBHs) with the **memory burden effect**, building on:

- **Montefalcone et al.** (2026), *Phys. Rev. D* **113**, 023524, arXiv:2503.21005 [astro-ph.CO] — *"Can a Breakdown of Hawking Evaporation Open a New Mass Window for Primordial Black Holes as Dark Matter?"*

This repository accompanies an ongoing study on phenomenological modeling of the continuous crossover from the semi-classical phase to the memory-burden phase in PBH evaporation.

## Key Features

| Task | Status |
|:---|:---|
| BBN constraint via decaying-particle mapping | :white_check_mark: |
| CMB + BBN combined constraints (reproducing Fig. 3 of Montefalcone+2026) | :white_check_mark: |
| Four smooth transition functions validation (additive & multiplicative) | :white_check_mark: |

## Code

[pbh_memory_burden_CN.ipynb](pbh_memory_burden_CN.ipynb) — Jupyter notebook with the complete code. Run all cells to generate the 7 result figures.

## Requirements

```bash
pip install numpy scipy matplotlib
```

## Quick Start

```bash
pip install numpy scipy matplotlib
jupyter notebook pbh_memory_burden_CN.ipynb
```

Then run all cells in the notebook to generate the 7 result figures.

## Physical Methods

- **BBN**: Decaying-particle mapping (Keith+2020, Kawasaki+2018)
- **CMB**: Three-phase independent calculation (Acharya+2020)
- **Combined**: f_combined = min(f_CMB, f_BBN)

### Key Parameters

| Parameter | Description | Typical Values |
|:---|:---|:---|
| `q` | Transition mass fraction (M_trans = q * M_i) | 0.2, 0.5, 0.8 |
| `delta` | Transition width (smoothness); delta=0 = step-like | 0, 0.1, 0.3 |
| `k` | Memory-burden power-law exponent | 2 |

## Output Figures

| Figure | Description |
|:---|:---|
| `pbh_cmb_fixed.png` | CMB constraints for different (q, delta) parameters |
| `bbn_constraint_plot.png` | BBN constraints for different (q, delta) parameters |
| `fig3_reproduction.png` | Combined CMB+BBN constraints (reproduces Fig. 3 of Montefalcone+2026) |
| `delta_scan.png` | Parameter scan varying delta (fixed q=0.5) |
| `q_scan.png` | Parameter scan varying q (fixed delta=0.1) |
| `four_transitions_comparison.png` | Comparison of 4 transition functions x 2 distributions |
| `abundance_enhancement.png` | Enhancement ratio f_new / f_default |

## References

- Acharya & Khatri (2020), *JCAP* **06**, 018, arXiv:2002.00898
- Kawasaki et al. (2018), *Phys. Rev. D* **97**, 023502
- Keith et al. (2020), *Phys. Rev. D* **102**, 103512
- Montefalcone et al. (2026), *Phys. Rev. D* **113**, 023524, arXiv:2503.21005 [astro-ph.CO]
