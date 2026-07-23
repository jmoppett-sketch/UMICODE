"""
Candidate UMI generation.

This module generates candidate molecular identifiers prior to
biological filtering and codebook optimisation.
"""

import random

from .models import UMI
from .validators import validate_generation_parameters

def generate_candidate_umis(
    number: int,
    length: int,
) -> list[UMI]:
    """
    Generate random candidate UMI sequences.

    Parameters
    ----------
    number
        Number of candidate UMIs to generate.

    length
        Length of each UMI.

    Returns
    -------
    list[UMI]
        Candidate UMI objects.
    """

    validate_generation_parameters(number, length)
    
    alphabet = "ACGT"

    candidates = []

    for _ in range(number):

        sequence = "".join(
        random.choice(alphabet)
        for _ in range(length)
    )

        candidates.append(
        UMI(
            length=length,
            sequence=sequence,
        )
    )

    return candidates