# pbh-memory-burden-constraints

Reproducing cosmological constraints on evaporating primordial black holes (PBHs) 
with the **memory burden effect**, based on Montefalcone+2026 (*Phys. Rev. D* **113**, 023524).

## Key Results

| Task | Status |
|:---|:---|
| BBN constraint via decaying-particle mapping | ✅ |
| CMB + BBN combined constraints (Fig. 3) | ✅ |
| Four transition functions validation | ✅ |

## Jupyter Notebook

📓 [Jupyter Notebook 完整代码与结果](https://nbviewer.jupyter.org/github/Yang-Meiting/pbh-memory-burden-constraints/blob/main/pbh_memory_burden_CN.ipynb)

## Modules

| File | Description |
|:---|:---|
| `pbh_bbn_v2.py` | BBN constraint (decaying-particle mapping) |
| `pbh_combined.py` | CMB + BBN merged constraints |
| `pbh_four_transitions.py` | Four transition functions comparison |
| `pbh_cmb_fixed.py` | CMB constraint module |

## Physical Methods

- **BBN**: Decaying-particle mapping ([29] Keith+2020, [37] Kawasaki+2018)
- **CMB**: Three-phase independent calculation ([22] Acharya+2019)
- **Combined**: `f = min(f_CMB, f_BBN)`
