# pbh-memory-burden-constraints

Reproducing cosmological constraints on evaporating primordial black holes (PBHs) with the **memory burden effect**, based on Montefalcone+2026 (*Phys. Rev. D* **113**, 023524).

## Key Results

| Task | Status |
|:---|:---|
| BBN constraint via decaying-particle mapping | ✅ |
| CMB + BBN combined constraints (Fig. 3) | ✅ |
| Four transition functions validation | ✅ |

## Jupyter Notebook

📓 [完整代码与结果](https://nbviewer.jupyter.org/github/Yang-Meiting/pbh-memory-burden-constraints/blob/main/pbh_memory_burden_CN.ipynb)

Notebook 内含全部 6 张结果图（base64 内嵌），无需额外下载即可查看。

## Physical Methods

- **BBN**: Decaying-particle mapping (Keith+2020, Kawasaki+2018)
- **CMB**: Three-phase independent calculation (Acharya+2019)
- **Combined**: $f_{\text{combined}} = \min(f_{\text{CMB}}, f_{\text{BBN}})$

## References

- Acharya et al. (2019), *Phys. Rev. D* **100**, 123524
- Kawasaki et al. (2018), *Phys. Rev. D* **97**, 023517
- Keith et al. (2020), *Phys. Rev. D* **102**, 123538
- Montefalcone et al. (2026), *Phys. Rev. D* **113**, 02352419)
- **Combined**: `f = min(f_CMB, f_BBN)`
