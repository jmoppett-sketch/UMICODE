# MRDUMICODE -- Project Kick-off

*Date:* 20 July 2026

## Vision

Develop **MRDUMICODE**, an ONT-aware duplex UMI design framework for
ultra-deep capture-based MRD detection (initial focus: Ig/TCR).

Core philosophy: - Design for the ONT error channel rather than simple
Hamming distance. - Co-design chemistry and decoding. - Build
incrementally with reproducible, well-tested software.

## Scientific decisions made

-   Initial platform: Oxford Nanopore Technologies (ONT).
-   Application: Capture-based Ig/TCR MRD.
-   Duplex UMIs with independent left and right codebooks.
-   Anchor sequences designed before UMI selection.
-   Candidate UMIs filtered against anchor and cassette constraints.
-   Begin with published ONT error models; later support empirical
    retraining.
-   Build a toy implementation before scaling.

## Planned architecture

Cassette:

Adapter → Anchor → Spacer → UMI → Insert → UMI → Spacer → Anchor →
Adapter

Future work: - Whole-cassette optimisation. - Channel-model
optimisation. - Probabilistic decoder. - ONT simulator.

## Repository

MRDUMICODE/

-   PROJECT.md
-   SPECIFICATION.md
-   ROADMAP.md
-   DECISIONS.md
-   IDEAS.md
-   src/
-   tests/
-   docs/
-   examples/

## Version roadmap

### V0.1

-   Repository skeleton
-   Candidate generator
-   Sequence filters
-   Anchor optimiser
-   Codebook optimiser
-   Toy library (32--64 UMIs)
-   Unit tests

### V0.2

-   ONT error simulator
-   Decoder
-   Monte Carlo benchmarking

### V0.3

-   Empirical ONT error model
-   Iterative optimisation from pilot data

## Immediate next session

1.  Create GitHub repository.
2.  Write SPECIFICATION.md.
3.  Create Python package skeleton.
4.  Implement candidate generator.
5.  Implement filtering engine.
6.  Build first toy codebook.
7.  Review outputs before optimisation.

## Guiding principle

First make it **correct**. Then make it **elegant**. Finally make it
**fast**.
