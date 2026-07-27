# Experiment 001 — Greedy UMI Codebook Optimiser Benchmark

## Objective

To evaluate whether the UMICODE optimisation algorithm improves UMI codebook quality compared with random selection from the same candidate pool.

The primary optimisation objective was maximisation of the minimum pairwise Hamming distance between UMIs in the final codebook.

The rationale is that the minimum distance represents the worst-case separation between any two UMIs and therefore the limiting factor for error correction and assignment ambiguity.

---

## Experimental design

### Candidate generation

A candidate pool of random UMI sequences was generated.

Parameters:

- UMI length: 16 nucleotides
- Candidate pool size: 5,000 UMIs
- Codebook size: 96 UMIs

Each candidate was represented as a UMI object within the UMICODE framework.

---

## Comparison groups

Two codebook selection approaches were compared:

### 1. Random codebook

A codebook of 96 UMIs was selected randomly from the candidate pool.

Random selection was controlled using a reproducible random seed.

### 2. Optimised codebook

A codebook of 96 UMIs was selected using the UMICODE optimisation algorithm.

The optimiser selected UMIs sequentially to maximise separation from the existing codebook.

---

## Evaluation metrics

Three metrics were assessed:

### Minimum pairwise distance

The smallest Hamming distance between any pair of UMIs within the codebook.

This represents the worst-case separation.

Higher values indicate improved error tolerance.

### Mean pairwise distance

The average Hamming distance across all UMI pairs.

This represents overall sequence diversity.

### Reproducibility

The experiment was repeated across multiple random seeds.

---

## Experimental parameters

- Number of replicates: 10
- Random seeds: 0–9
- Python version: 3.14.4
- Runtime: 349.62 seconds

---

# Results

## Minimum pairwise distance

### Random codebooks

Values:
