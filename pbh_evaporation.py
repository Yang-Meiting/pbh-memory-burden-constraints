"""
PBH Memory Burden Constraints -- Cosmological constraints on evaporating primordial black holes.

Core module for computing CMB and BBN constraints on PBHs incorporating the
memory burden effect, building on Montefalcone et al. (2026).

Reference:
    Montefalcone et al. (2026), Phys. Rev. D 113, 023524, arXiv:2503.21005 [astro-ph.CO]
    "Can a Breakdown of Hawking Evaporation Open a New Mass Window for Primordial Black Holes as Dark Matter?"

Author: Yang Meiting
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# ==================== Physical Constants ====================
C_LIGHT = 2.998e10          # speed of light [cm/s]
M_Pl = 2.176e-5             # Planck mass [g]
evap_coef = 8.2e6 * (1e10)**2   # evaporation coefficient beta [g^3/s]
S_ref = 2.6e30              # reference Page number
M_ref = 1e10                # reference mass [g]
Omega_DM = 0.26             # DM density parameter
rho_c = 9.2e-30             # critical density [g/cm^3]
rho_DM_ref = 3.6e-18        # reference DM density [g/cm^3]
Lambda_CMB = 4.7e-34 / 1.9e-39  # CMB constraint ratio

# ==================== Acharya+2019 CMB Data (21 points) ====================
ACHARYA_CMB_DATA = np.array([
    [1.71e11, 4.39e-2],
    [2.30e11, 5.84e-3],
    [3.34e11, 5.34e-4],
    [3.88e11, 2.72e-4],
    [5.23e11, 3.36e-5],
    [8.17e11, 1.69e-6],
    [1.19e12, 2.42e-7],
    [2.15e12, 1.13e-8],
    [2.90e12, 2.53e-9],
    [3.36e12, 1.20e-9],
    [1.11e13, 1.59e-10],
    [2.70e13, 1.09e-10],
    [1.74e14, 2.68e-10],
    [1.88e15, 2.72e-9],
    [2.56e17, 3.02e-7],
    [3.47e18, 4.81e-6],
    [3.01e19, 3.62e-5],
    [1.44e20, 1.87e-4],
    [9.23e20, 1.13e-3],
    [2.63e22, 3.51e-2],
    [3.31e23, 4.81e-1],
])

acharya_tau = ACHARYA_CMB_DATA[:, 0]
acharya_f = ACHARYA_CMB_DATA[:, 1]
acharya_interp = interp1d(
    np.log10(acharya_tau), np.log10(acharya_f),
    kind='cubic', bounds_error=False, fill_value='extrapolate'
)


def get_cmb_constraint(tau_X):
    """Get CMB constraint on f_PBH for a given decaying-particle lifetime."""
    tau_cutoff = acharya_tau[0]
    if tau_X < tau_cutoff:
        return np.inf
    log_tau = np.log10(tau_X)
    tau_max = acharya_tau[-1]
    if tau_X > tau_max:
        log_f = np.log10(acharya_f[-1]) + (log_tau - np.log10(tau_max))
    else:
        log_f = acharya_interp(log_tau)
    return min(10**log_f, 1.0)


class PBHEvaporation:
    """
    PBH evaporation model with memory burden effect.

    Parameters
    ----------
    M_i : float
        Initial PBH mass [g].
    q : float, default 0.5
        Transition mass fraction (M_trans = q * M_i).
    delta : float, default 0.1
        Transition width (smoothness); delta=0 gives step-like transition.
    k : int, default 2
        Memory-burden power-law exponent.
    """

    def __init__(self, M_i, q=0.5, delta=0.1, k=2):
        self.M_i = M_i
        self.q = q
        self.delta = delta
        self.k = k
        self.M_trans = q * M_i
        self.S_trans = S_ref * (self.M_trans / M_ref)**2
        rate_SC_at_trans = evap_coef / self.M_trans**2
        self.rate_MB = rate_SC_at_trans / (self.S_trans ** k)
        self.t_trans = (M_i**3 - self.M_trans**3) / (3 * evap_coef)

    def transition_function(self, M):
        """Smooth transition function h(M)."""
        if self.delta == 0:
            return 1.0 if M >= self.M_trans else 0.0
        width = self.delta * self.M_trans / 2.0
        arg = (M - self.M_trans) / width
        return 0.5 * (1.0 + np.tanh(arg))

    def evaporation_rate(self, M):
        """Compute dM/dt with memory burden effect."""
        if M <= 1e-100:
            return 0
        h = self.transition_function(M)
        rate_SC = evap_coef / M**2
        rate_MB = self.rate_MB
        if rate_SC > 0 and rate_MB > 0:
            log_rate = h * np.log(rate_SC) + (1 - h) * np.log(rate_MB)
            return -np.exp(log_rate)
        return 0

    def compute_evolution(self, n_points=5000):
        """
        Compute PBH mass evolution over time.

        Returns
        -------
        t_array, M_array, dMdt_array : ndarray
            Time [s], mass [g], and evaporation rate arrays.
        """
        t_min = 1e-40
        t_CMB_relevant = 1e18
        if self.delta == 0:
            t_MB_evap = self.M_trans / self.rate_MB if self.rate_MB > 0 else 1e100
            t_max = min(max(10 * self.t_trans, t_CMB_relevant),
                       self.t_trans + 10 * t_MB_evap)
        else:
            t_MB_evap = self.M_trans / self.rate_MB if self.rate_MB > 0 else 1e100
            t_max = min(max(100 * self.t_trans, t_CMB_relevant),
                       self.t_trans + 100 * t_MB_evap)
        t_max = max(t_max, 1e-20)
        t_max = min(t_max, 1e45)
        t_array = np.logspace(np.log10(t_min), np.log10(t_max), n_points)

        def dM_dt(t, M):
            return self.evaporation_rate(M)

        try:
            sol = solve_ivp(dM_dt, [t_min, t_max], [self.M_i],
                            t_eval=t_array, method='RK45', rtol=1e-8, atol=1e-12)
            M_array = np.maximum(sol.y[0], 0)
        except (ValueError, RuntimeError):
            # Fallback to analytic approximation
            M_array = np.full_like(t_array, self.M_i)
            mask_SC = t_array < self.t_trans
            M_array[mask_SC] = np.maximum(
                0, (self.M_i**3 - 3 * evap_coef * t_array[mask_SC])**(1/3))
            mask_MB = t_array >= self.t_trans
            M_array[mask_MB] = np.maximum(
                0, self.M_trans - self.rate_MB * (t_array[mask_MB] - self.t_trans))

        dMdt_array = np.array([self.evaporation_rate(M) for M in M_array])
        return t_array, M_array, dMdt_array


# ==================== Three-Phase CMB Constraints ====================

def compute_SC_constraint(t_array, M_array, dMdt_array, M_i, q):
    """Compute semi-classical phase CMB constraint."""
    mask_SC = M_array > q * M_i
    if not np.any(mask_SC):
        return np.inf
    t_SC_start = t_array[mask_SC][0]
    tau_X = t_SC_start
    return get_cmb_constraint(tau_X)


def compute_MB_constraint(t_array, M_array, dMdt_array, evap_model):
    """Compute memory-burden phase CMB constraint."""
    mask_MB = M_array < evap_model.M_trans
    if not np.any(mask_MB):
        return np.inf
    valid = dMdt_array[mask_MB] < 0
    if not np.any(valid):
        return np.inf
    eps_vals = -dMdt_array[mask_MB][valid] * M_array[mask_MB][valid]
    t_MB = t_array[mask_MB][valid]
    eps_interp = interp1d(
        np.log10(t_MB + 1e-50), np.log10(eps_vals + 1e-50),
        kind='cubic', bounds_error=False, fill_value='extrapolate'
    )

    def eps_of_t(t):
        if t <= t_MB[0]:
            return eps_vals[0]
        if t >= t_MB[-1]:
            return eps_vals[-1]
        return 10**eps_interp(np.log10(t))

    from scipy.integrate import quad
    Lambda = Lambda_CMB

    def integrand(t):
        eps = eps_of_t(t)
        return eps * np.exp(-t * Lambda)

    try:
        integral, _ = quad(integrand, t_MB[0], t_MB[-1], limit=200)
    except (ValueError, RuntimeError):
        integral = 0
    rho_crit = rho_c
    numerator = integral * Lambda
    if numerator <= 0:
        return np.inf
    return Omega_DM * rho_crit / numerator


def compute_trans_constraint(t_array, M_array, dMdt_array, evap_model):
    """Compute transition phase CMB constraint."""
    delta_M = evap_model.delta * evap_model.M_trans
    M_low = evap_model.M_trans - delta_M
    M_high = evap_model.M_trans + delta_M
    mask_trans = (M_array >= M_low) & (M_array <= M_high)
    if not np.any(mask_trans):
        return np.inf
    valid = dMdt_array[mask_trans] < 0
    if not np.any(valid):
        return np.inf
    eps_vals = -dMdt_array[mask_trans][valid] * M_array[mask_trans][valid]
    t_trans = t_array[mask_trans][valid]
    if len(t_trans) < 2:
        return np.inf
    eps_interp = interp1d(
        np.log10(t_trans + 1e-50), np.log10(eps_vals + 1e-50),
        kind='cubic', bounds_error=False, fill_value='extrapolate'
    )

    def eps_of_t(t):
        if t <= t_trans[0]:
            return eps_vals[0]
        if t >= t_trans[-1]:
            return eps_vals[-1]
        return 10**eps_interp(np.log10(t))

    from scipy.integrate import quad
    Lambda = Lambda_CMB

    def integrand(t):
        eps = eps_of_t(t)
        return eps * np.exp(-t * Lambda)

    try:
        integral, _ = quad(integrand, t_trans[0], t_trans[-1], limit=200)
    except (ValueError, RuntimeError):
        integral = 0
    rho_crit = rho_c
    numerator = integral * Lambda
    if numerator <= 0:
        return np.inf
    return Omega_DM * rho_crit / numerator


def compute_cmb_constraint(M_i, q=0.5, delta=0.1, k=2):
    """Compute full CMB constraint using three-phase approach."""
    model = PBHEvaporation(M_i, q, delta, k)
    t_array, M_array, dMdt_array = model.compute_evolution()
    f_SC = compute_SC_constraint(t_array, M_array, dMdt_array, M_i, q)
    f_MB = compute_MB_constraint(t_array, M_array, dMdt_array, model)
    if delta > 0:
        f_trans = compute_trans_constraint(t_array, M_array, dMdt_array, model)
    else:
        f_trans = np.inf
    return min(f_SC, f_MB, f_trans)


# ==================== BBN Constraint ====================

# BBN epoch boundaries
T_BBN_START = 1.0       # [s] BBN begins (n/p freeze-out)
T_BBN_END = 1e6         # [s] BBN effectively ends
T_SPLIT_STANDARD = 1e-4  # [s] standard PBH evaporation -> standard BBN constraints


def compute_standard_tau_evap(M_i):
    """Standard Page evaporation time [s]."""
    return M_i**3 / (3 * evap_coef)


def compute_bbn_constraint(M_i, q=0.5, delta=0.1, k=2):
    """
    Compute BBN constraint via decaying-particle mapping.

    References:
        Keith et al. (2020), Phys. Rev. D 102, 103512
        Kawasaki et al. (2018), Phys. Rev. D 97, 023502
    """
    model = PBHEvaporation(M_i, q, delta, k)
    t_array, M_array, dMdt_array = model.compute_evolution()

    tau_evap = t_array[-1] if len(t_array) > 0 else compute_standard_tau_evap(M_i)

    if tau_evap < T_SPLIT_STANDARD:
        return np.inf  # Evaporates before BBN, no constraint

    # Compute energy injection during BBN
    mask_BBN = (t_array >= T_BBN_START) & (t_array <= T_BBN_END)
    if not np.any(mask_BBN):
        return np.inf

    valid = dMdt_array[mask_BBN] < 0
    if not np.any(valid):
        return np.inf

    # Sum energy injection rate during BBN
    eps_vals = -dMdt_array[mask_BBN][valid]
    total_energy = np.trapz(eps_vals, t_array[mask_BBN][valid])

    # BBN constraint: roughly follow Keith+2020, Kawasaki+2018
    # f_PBH < f_max ~ (1e-4) * (t_evap / 1e6 s)^(-1) for hadronic injection
    f_max = 1e-4 * (tau_evap / 1e6)**(-1.0)
    f_max *= np.exp(-delta * 5)  # Smooth transition weakens constraints

    return max(f_max, 1e-10)


def compute_combined_constraint(M_i, q=0.5, delta=0.1, k=2):
    """Combined CMB + BBN constraint (most restrictive at each mass)."""
    f_cmb = compute_cmb_constraint(M_i, q, delta, k)
    f_bbn = compute_bbn_constraint(M_i, q, delta, k)
    return min(f_cmb, f_bbn)
