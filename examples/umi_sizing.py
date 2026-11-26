"""UMI sizing for the anchored-ligation ONT MRD assay (26 Nov 2026).

Answers: how long does a degenerate UMI need to be, and does it need a designed
distance codebook, when molecules are identified by (UMI, shear point)?

Three steps:
  1. effective number of shear-point bins (how much the random shear point helps)
  2. molecules sharing one shear window  -> how many UMIs must be told apart
  3. P(two random UMIs within edit distance k) for candidate patterns

Run:  python3 examples/umi_sizing.py            (about 2-4 min with edlib)
      python3 examples/umi_sizing.py --pairs 200000   (quicker, noisier)
Needs: numpy, edlib  (pip install numpy edlib)
"""
from __future__ import annotations

import argparse
import re

import edlib
import numpy as np

# IUPAC mixed-base codes as an oligo vendor uses them.
IUPAC = {"N": "ACGT", "V": "ACG", "H": "ACT", "D": "AGT", "B": "CGT",
         "A": "A", "C": "C", "G": "G", "T": "T"}

PATTERNS = {
    "N12": "N" * 12,
    "N16": "N" * 16,
    "N24": "N" * 24,
    # No base is allowed at all four positions of VHDB, so no run can exceed 3.
    "VHDBx7 (28 nt)": "VHDB" * 7,
}


def anchor_to_shear_distances(mean_bp: float, n: int, rng, cv: float = 0.5) -> np.ndarray:
    """Distance from an anchor primer to its fragment's shear point.

    Fragments are log-normal. Fragments that contain an anchor are picked in
    proportion to their length (a long fragment is more likely to contain it),
    and the anchor sits uniformly within the fragment.
    """
    sigma = np.sqrt(np.log(1 + cv ** 2))
    mu = np.log(mean_bp) - sigma ** 2 / 2
    pool = rng.lognormal(mu, sigma, n * 3)
    lengths = rng.choice(pool, n, p=pool / pool.sum())   # length-biased sampling
    return rng.uniform(0, lengths)


def effective_bins(distances: np.ndarray, resolution_bp: int) -> float:
    """1 / sum(p^2): the number of equally likely bins with the same collision rate.

    Teaching note: this is the inverse Simpson index from ecology. Two molecules
    land in the same bin with probability sum(p^2), so 1/sum(p^2) is the number of
    equal bins that would give the same chance.
    """
    counts = np.bincount((distances // resolution_bp).astype(int))
    p = counts / counts.sum()
    return 1.0 / np.sum(p ** 2)


def random_umis(pattern: str, n: int, rng) -> list[str]:
    cols = [np.array(list(IUPAC[c]))[rng.integers(0, len(IUPAC[c]), n)] for c in pattern]
    return ["".join(row) for row in np.stack(cols, axis=1)]


def near_collision_probs(pattern: str, pairs: int, rng, ks=(4, 5, 6)) -> dict[int, float]:
    a, b = random_umis(pattern, pairs, rng), random_umis(pattern, pairs, rng)
    kmax = max(ks)
    d = np.array([edlib.align(x, y, task="distance", k=kmax)["editDistance"] for x, y in zip(a, b)])
    d[d < 0] = kmax + 1                      # edlib returns -1 when distance > k
    return {k: float(np.mean(d <= k)) for k in ks}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--molecules", type=float, default=1e6, help="identical molecules per anchor (albumin)")
    ap.add_argument("--mean-bp", type=float, default=8000, help="mean fragment length")
    ap.add_argument("--resolution", type=int, default=10, help="shear-point resolution, bp")
    ap.add_argument("--window-bins", type=int, default=3, help="bins compared (+/-1 for jitter)")
    ap.add_argument("--pairs", type=int, default=1_000_000, help="Monte Carlo UMI pairs")
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)       # fixed seed: same numbers every run

    bins = effective_bins(anchor_to_shear_distances(args.mean_bp, 2_000_000, rng), args.resolution)
    per_window = args.window_bins * args.molecules / bins
    print(f"effective shear bins: {bins:,.0f}  (mean {args.mean_bp:.0f} bp, {args.resolution} bp resolution)")
    print(f"molecules per shear window: {per_window:,.0f}\n")

    print(f"{'pattern':16s} {'log10 space':>11s} {'P(hp>=4)':>9s}  "
          f"{'P(ED<=4)':>9s} {'P(ED<=5)':>9s} {'P(ED<=6)':>9s}  confused/molecule @ED<=5")
    for name, pat in PATTERNS.items():
        space = sum(np.log10(len(IUPAC[c])) for c in pat)
        sample = random_umis(pat, 100_000, rng)
        hp = np.mean([bool(re.search(r"A{4,}|C{4,}|G{4,}|T{4,}", s)) for s in sample])
        p = near_collision_probs(pat, args.pairs, rng)
        print(f"{name:16s} {space:11.1f} {hp:9.3f}  {p[4]:9.1e} {p[5]:9.1e} {p[6]:9.1e}  {per_window * p[5]:.3g}")


if __name__ == "__main__":
    main()
