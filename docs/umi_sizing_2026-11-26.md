# UMI sizing for the anchored-ligation assay

*26 November 2026. Provenance: [JM] = John's decision or position; [Claude] = analysis or
suggestion. Script: `examples/umi_sizing.py` (fixed seed; numbers below from it).*

## What changed in the assay

The ONT MRD assay moved from hybrid capture to anchored ligation (`ont-igtcr-mrd`, protocol
addendum 30 Oct 2026). Consequences for this repo [Claude, agreed by JM]:

- **One UMI per molecule.** The anchor end is primed, not ligated, and only one strand is
  templated. The duplex left/right cassette in `docs/Specification` does not fit this
  chemistry.
- **The random shear point is a second identifier.** A molecule is (UMI, shear point, anchor),
  so a UMI only has to be distinguishable from molecules sharing its shear window.

## Numbers [Claude]

Design case: ~10⁶ identical albumin molecules per sample (the denominator). Clone molecules at
follow-up are too few to collide.

**Effective shear bins** (log-normal fragments, CV 0.5, length-biased, anchor uniform):

| Mean fragment | 5 bp resolution | 10 bp | 20 bp |
|---|---|---|---|
| 8 kb | 2,166 | 1,083 | 542 |
| 2.5 kb | 677 | 339 | 169 |

At 8 kb, 10 bp, ±1 bin: **~2,800 molecules per shear window.**

**Near-collisions between random UMIs** (10⁶ Monte Carlo pairs; edit distance ~5 is the
raw-read clustering tolerance at ~2% error):

| UMI | Space | P(homopolymer ≥4) | P(ED ≤5) | P(ED ≤6) | Confused per molecule |
|---|---|---|---|---|---|
| N12 | 1.7×10⁷ | — | 0.04 | 0.16 | ≫1 |
| N16 | 4×10⁹ | — | 1×10⁻³ | 7.5×10⁻³ | ~3–20 |
| N24 | 3×10¹⁴ | 0.23 | 1×10⁻⁶ | 6×10⁻⁶ | 0.3–1.7% |
| **(VHDB)×7, 28 nt** | **2×10¹³** | **0** | 1×10⁻⁶ | 4×10⁻⁶ | **0.3–1.1%** |

## Conclusions

1. **Degenerate, not a distance codebook** [Claude; JM agreed]. A min-distance codebook at
   L≈24 is limited to ~10⁴–10⁵ words, giving 3–30% *exact* collisions at 2,800 molecules per
   window. Random long UMIs have essentially no exact collisions and a ~1% near-miss rate.
   The "as far apart as possible" principle (JM's earlier publication) still holds for small
   sets that must be unmistakable: sample barcodes, and the fixed flanks that locate the UMI.
2. **28 nt (VHDB)×7** [JM agreed]. V, H, D, B each exclude one base and no base is in all
   four, so homopolymers are capped at 3, the main ONT error mode. Orderable as standard
   mixed bases (IDT).
3. **Where it sits** [JM, Claude]: on the arm-A (T-overhang) strand of a Y-adaptor, single
   stranded in the fork. Spec and annealing protocol: `ont-igtcr-mrd` SOP 2.2.

## Assumptions to measure in the pilot

- Shear-point resolution ±10 bp: the most important assumption. Measure as the spread of
  read-end positions within albumin UMI families.
- ~2% raw error in UMI sequence on R10.4.1 sup.
- Uniform synthesis of mixed bases (machine mix skews ~T 30 : G 26 : C 24 : A 20 for N; small
  effect at 10¹³).
- ~10⁶ albumin molecules per sample. At 2.5 kb fragments the window load triples: use 32 nt.

## Effect on this repo's roadmap

The duplex L/R codebook and anchor-first optimisation remain valid code but are not on the
assay's critical path. The useful next pieces are a decoder that groups reads by
(UMI, shear point) and the measured error curve (e vs reads per molecule) the handoff asks for.
