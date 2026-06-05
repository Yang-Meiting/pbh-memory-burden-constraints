# PBH Memory Burden Constraints

Numerical tools for cosmological constraints on evaporating primordial black holes (PBHs) with the memory burden effect.

This repository accompanies the undergraduate research project:

> **原初黑洞作为暗物质候选者及其质量起源研究**  
> *Primordial Black Holes as Dark Matter Candidates and the Origin of Their Masses*  
> Supported by the Provincial Undergraduate Innovation and Entrepreneurship Training Program (省级大学生创新创业训练计划)  
> Project period: 2025.05 -- present  

## Published Paper

The following paper is a spin-off result from this project:

> **"BBN constraints on primordial black holes with a continuous memory-burden crossover"**  
> X.-Y. Zhang, M.-T. Yang, H.-B. Jin  
> arXiv:2606.04707 [astro-ph.CO] (2026)

The published paper focuses specifically on **BBN constraints** computed with AlterBBN, using a smooth tanh crossover profile and comparing additive versus multiplicative rate combinations. Earlier numerical explorations in this repository (e.g., CMB constraints, four-transition-function comparisons) were part of the project's initial investigation phase and are **not** included in the published paper.

## Repository Overview

| Component | Description |
|-----------|-------------|
| `pbh_evaporation.py` | Core module: PBH evaporation model with memory-burden effect |
| `pbh_memory_burden.ipynb` | Main analysis notebook (English) |

### Research phases reflected in the code

| Phase | Content | Key features |
|-------|---------|--------------|
| **Initial exploration** | Python-based numerical prototyping | CMB constraints (three-phase); BBN constraints (decaying-particle mapping); four transition functions (tanh, erf, arctan, fractional radical) |
| **Focused study** | AlterBBN-based BBN analysis | Smooth tanh crossover; additive vs. multiplicative rate combinations; parameter scans in $(q, \delta)$ |

The **focused study** corresponds to the published paper arXiv:2606.04707.

## Quick Start

```bash
pip install -r requirements.txt
jupyter notebook pbh_memory_burden.ipynb
```

Then run all cells in the notebook to generate the result figures.

## Physical Methods

- **BBN constraints**: Decaying-particle mapping following Keith et al. (2020), Kawasaki et al. (2018). The published paper uses Modified AlterBBN for the actual calculation; this repository also includes a Python prototype implementation.
- **CMB constraints**: Three-phase calculation (semi-classical + transition + memory-burden) based on Acharya & Khatri (2020) data. This is part of the project's initial exploration and is **not** in the published paper.

## Key Parameters

| Parameter | Description | Typical Values |
|-----------|-------------|----------------|
| `q` | Transition mass fraction ($M_{\rm trans} = q \, M_i$) | 0.2, 0.5, 0.8 |
| `delta` | Transition width (smoothness); `delta=0` = step-like | 0, 0.1, 0.3 |
| `k` | Memory-burden power-law exponent | 2 |

## Output Figures

| Figure | Description |
|--------|-------------|
| `bbn_constraint_plot.png` | BBN constraints for different $(q, \delta)$ |
| `delta_scan.png` | Parameter scan varying $\delta$ (fixed $q=0.5$) |
| `q_scan.png` | Parameter scan varying $q$ (fixed $\delta=0.1$) |
| `fig3_reproduction.png` | Combined CMB+BBN constraints (initial exploration; published paper shows BBN only) |
| `pbh_cmb_fixed.png` | CMB constraints for different $(q, \delta)$ (initial exploration) |
| `four_transitions_comparison.png` | Four transition functions $\times$ two distributions (initial exploration) |
| `abundance_enhancement.png` | Enhancement ratio $f_{\rm new} / f_{\rm default}$ (initial exploration) |

## References

- Zhang, Yang & Jin (2026), arXiv:2606.04707 [astro-ph.CO]
- Montefalcone, G., Hooper, D., Freese, K., Kelso, C., Kühnel, F., & Sandick, P. (2026). 
  *Can a breakdown of Hawking evaporation open a new mass window for primordial black holes as dark matter?* 
  Phys. Rev. D, 113(2), 023524. DOI: [10.1103/PhysRevD.113.023524](https://doi.org/10.1103/PhysRevD.113.023524)
  arXiv: [2503.21005](https://arxiv.org/abs/2503.21005)
- Acharya, S. K., & Khatri, R. (2020). 
  *CMB and BBN constraints on evaporating primordial black holes revisited.* 
  JCAP, 06, 018. DOI: [10.1088/1475-7516/2020/06/018](https://doi.org/10.1088/1475-7516/2020/06/018)
  arXiv: [2002.00898](https://arxiv.org/abs/2002.00898)
- Kawasaki et al. (2018), Phys. Rev. D 97, 023502
- Keith et al. (2020), Phys. Rev. D 102, 103512

## License

MIT License
