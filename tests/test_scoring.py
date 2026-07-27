import pytest

from umicode.scoring import hamming_distance
from umicode.models import UMI
from umicode.scoring import (
    hamming_distance,
    minimum_pairwise_distance, mean_pairwise_distance
)
# ---------------------------------------------------------------------
# Hamming distance
# ---------------------------------------------------------------------

def test_hamming_distance_identical():

    assert hamming_distance(
        "ATCG",
        "ATCG",
    ) == 0

def test_hamming_distance_single_difference():

    assert hamming_distance(
        "ATCG",
        "ATGG",
    ) == 1

def test_hamming_distance_all_different():

    assert hamming_distance(
        "AAAA",
        "TTTT",
    ) == 4

def test_hamming_distance_requires_equal_length():

    with pytest.raises(ValueError):

        hamming_distance(
            "AAA",
            "AAAA",
        )
# ---------------------------------------------------------------------
# Minimum Pairwise distance
# ---------------------------------------------------------------------

def test_minimum_pairwise_distance_identical():

    umis = [
        UMI(length=4, sequence="ATCG"),
        UMI(length=4, sequence="ATCG"),
    ]

    assert minimum_pairwise_distance(umis) == 0

def test_minimum_pairwise_distance_three_umis():

    umis = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="AAAT"),
        UMI(length=4, sequence="TTTT"),
    ]

    assert minimum_pairwise_distance(umis) == 1

def test_minimum_pairwise_distance_well_separated():

    umis = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
        UMI(length=4, sequence="GGGG"),
    ]

    assert minimum_pairwise_distance(umis) == 4

def test_minimum_pairwise_distance_requires_two_umis():

    umis = [
        UMI(length=4, sequence="AAAA"),
    ]

    with pytest.raises(ValueError):

        minimum_pairwise_distance(umis)

def test_mean_pairwise_distance():

    umis = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="AAAT"),
        UMI(length=4, sequence="TTTT"),
    ]

    assert mean_pairwise_distance(
        umis,
    ) == 2.6666666666666665


def test_mean_pairwise_distance_requires_two_umis():

    umi = UMI(
        length=4,
        sequence="AAAA",
    )

    with pytest.raises(ValueError):

        mean_pairwise_distance(
            [umi],
        )
