from itertools import combinations

from .models import UMI

def hamming_distance(
    sequence_1: str,
    sequence_2: str,
) -> int:
    """
    Calculate the Hamming distance between two sequences.
    """

    if len(sequence_1) != len(sequence_2):
        raise ValueError(
            "Sequences must have equal length."
        )


    return sum(
        base_1 != base_2
        for base_1, base_2 in zip(
            sequence_1,
            sequence_2,
        )
    )


def minimum_pairwise_distance(
    umis: list[UMI],
) -> int:
    """
    Calculate the minimum Hamming distance between all
    pairs of UMIs in a codebook.
    """
    if len(umis) <2:
        raise ValueError("There must be at least 2 UMIs to compare")


    smallest = None
    for umi_1, umi_2 in combinations(umis, 2):
        distance = hamming_distance(
            umi_1.sequence,
            umi_2.sequence,
)
        if smallest is None or distance < smallest:
            smallest = distance

    return smallest
