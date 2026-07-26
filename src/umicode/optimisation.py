"""
Codebook optimisation algorithms.

Methods for selecting high-quality UMI codebooks from
candidate sequences.
"""

import random

from .models import UMI
from .scoring import hamming_distance



def minimum_distance_to_codebook(
    candidate: UMI,
    codebook: list[UMI],
) -> int:
    """
    Calculate the minimum distance between a candidate UMI
    and an existing codebook.
    """

    if len(codebook) == 0:
        raise ValueError(
            "Codebook must contain at least one UMI."
        )

    smallest = None

    for umi in codebook:

        distance = hamming_distance(
                candidate.sequence,
                umi.sequence,
        )

        if smallest is None or distance < smallest:
            smallest = distance

    return smallest



def optimise_codebook(
    candidates: list[UMI],
    size: int,
    seed: int | None = None,
) -> list[UMI]:
    """
    Select a high-quality UMI codebook from candidates.
    """

    def optimise_codebook(
    candidates: list[UMI],
    size: int,
    seed: int | None = None,
) -> list[UMI]:
    
        """
        Select a high-quality UMI codebook from candidates.
        """

    if size <= 0:
        raise ValueError(
            "Codebook size must be greater than zero."
        )

    if size > len(candidates):
        raise ValueError(
            "Codebook size cannot exceed number of candidates."
        )

    rng = random.Random(seed)

    remaining = candidates.copy()

    first = rng.choice(remaining)

    codebook = [first]

    remaining.remove(first)

    while len(codebook) < size:

        best_candidate = None
        best_distance = -1

        for candidate in remaining:

            distance = minimum_distance_to_codebook(
                candidate,
                codebook,
            )

            if distance > best_distance:
                best_distance = distance
                best_candidate = candidate

        codebook.append(best_candidate)
        remaining.remove(best_candidate)

    return codebook
