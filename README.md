# pbh-memory-burden-constraints

This repository reproduces cosmological constraints on evaporating primordial black holes (PBHs) with the **memory burden effect**, based on:

- **Primary reference** (method foundation): Montefalcone+2025 (arXiv:2503.21005 [astro-ph.CO]), *"Does Memory Burden Open a New Mass Window for PBHs as Dark Matter?"*
- **This work**: Zhang, Yang, and Jin (2025), *"Phenomenologically Modeling the Continuous Crossover of Primordial Black Holes under Memory-Burden Effect"*

## Key Results

| Task | Status |
|:---|:---|
| BBN constraint via decaying-particle mapping | :white_check_mark: |
| CMB + BBN combined constraints (Fig. 3) | :white_check_mark: |
| Four transition functions validation | :white_check_mark: |

## Jupyter Notebook

[Notebook](pbh_memory_burden_CN.ipynb)

Notebook contains all 6 result figures (base64 embedded); no additional downloads required.

## Physical Methods

- **BBN**: Decaying-particle mapping (Keith+2020, Kawasaki+2018)
- **CMB**: Three-phase independent calculation (Acharya+2019)
- **Combined**: f_combined = min(f_CMB, f_BBN)

## References

- Acharya et al. (2019), *Phys. Rev. D* **100**, 123524
- Kawasaki et al. (2018), *Phys. Rev. D* **97**, 023517
- Keith et al. (2020), *Phys. Rev. D* **102**, 123538
- Montefalcone et al. (2025), arXiv:2503.21005 [astro-ph.CO]
