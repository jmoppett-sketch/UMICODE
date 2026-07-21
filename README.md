UMICODE
A framework for designing and decoding error-aware duplex Unique Molecular Identifiers (UMIs) for long-read sequencing
Status: Early development (v0.0.1)

⚠️ This project is in active early development. The APIs, algorithms and repository structure are expected to evolve rapidly during the initial design phase.
 
Overview
UMICODE is an open-source framework for designing, simulating and decoding duplex Unique Molecular Identifiers (UMIs) for long-read sequencing.
The initial focus is Oxford Nanopore Technologies (ONT) and ultra-deep capture-based minimal residual disease (MRD) assays, particularly immunoglobulin (Ig) and T-cell receptor (TCR) targets. The longer-term goal is to provide a general framework for robust molecular identifier design across sequencing platforms.
Most existing UMI design approaches were developed for short-read sequencing and focus primarily on sequence distance metrics. UMICODE instead explores an alternative design philosophy based on explicit modelling of the sequencing error channel. 
 
Motivation
Current UMI designs are largely based on short-read sequencing assumptions, where substitution errors dominate and random nucleotide strings are generally sufficient.
Long-read sequencing introduces a different set of challenges:
•	insertion and deletion errors
•	sequence-context-dependent error rates
•	homopolymer-associated basecalling errors
•	duplex molecular identification
•	robust parsing of UMI boundaries
UMICODE explores a different philosophy:
•	design UMI codebooks specifically for the sequencing platform;
•	jointly optimise anchors, spacers and UMIs;
•	design molecular codebooks together with their decoder;
•	simulate realistic sequencing errors during optimisation.
 
Project Goals
Version 0.1
•	Candidate UMI generation
•	Sequence filtering
•	Anchor optimisation
•	Duplex codebook construction
•	Toy datasets
•	Unit testing
Version 0.2
•	ONT error simulator
•	Probabilistic decoder
•	Monte Carlo benchmarking
Version 0.3
•	Empirical ONT error model
•	Iterative codebook optimisation from pilot sequencing data
•	Decoder refinement using measured channel characteristics
 
Design Principles
UMICODE is built around several core principles.
•	Duplex UMIs with independent left and right codebooks.
•	Anchor sequences are designed before UMI selection.
•	Entire cassette architecture is considered during optimisation.
•	Optimisation targets sequencing-channel behaviour rather than simple sequence distance.
•	All workflows are reproducible and deterministic through fixed random seeds.
•	Every algorithm is accompanied by automated tests.
 
Repository Structure
docs/           Project documentation
examples/       Example datasets
notebooks/      Exploratory notebooks
src/            Python source code
tests/          Unit tests

docs/
    SPECIFICATION.md
    ROADMAP.md
    DECISIONS.md
    IDEAS.md
 
Long-term Vision
The long-term aim is to develop a complete encoder/decoder framework for molecular barcoding, including:
•	platform-aware codebook design;
•	probabilistic decoding;
•	realistic sequencing simulation;
•	empirical error model learning;
•	support for ONT, PacBio and short-read sequencing platforms.
Although the first application is Ig/TCR MRD, the underlying framework is intended to be broadly applicable to duplex sequencing, targeted oncology, immune repertoire sequencing and other ultra-sensitive molecular assays.
 
Development Status
This repository is currently in active early development.
The first milestone is to produce a complete proof-of-concept implementation capable of:
1.	generating constrained duplex UMI libraries;
2.	optimising anchor sequences;
3.	constructing robust codebooks;
4.	simulating sequencing errors; and
5.	recovering UMIs using an ONT-aware decoder.
 
Contributing
The project is currently under active development. Contributions, discussions and suggestions are welcome as the architecture matures.
 
Licence
This project will be released under the BSD 3-Clause License.
 
Citation
A formal software citation and associated publication will be added following the first public release.
