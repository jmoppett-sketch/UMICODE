from umicode.models import UMI
from umicode.optimisation import (
    minimum_distance_to_codebook,
    optimise_codebook,
)


def test_minimum_distance_to_codebook_finds_closest_umi():

    codebook = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
        UMI(length=4, sequence="GGGG"),
    ]

    candidate = UMI(
        length=4,
        sequence="AAAT",
    )

    assert minimum_distance_to_codebook(
        candidate,
        codebook,
    ) == 1

def test_minimum_distance_to_codebook_max_distance():

    codebook = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
    ]

    candidate = UMI(
        length=4,
        sequence="GGGG",
    )

    assert minimum_distance_to_codebook(
        candidate,
        codebook,
    ) == 4

import pytest


def test_minimum_distance_requires_existing_codebook():

    candidate = UMI(
        length=4,
        sequence="AAAA",
    )

    with pytest.raises(ValueError):

        minimum_distance_to_codebook(
            candidate,
            [],
        )

def test_minimum_distance_to_codebook_identical_candidate():

    codebook = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
    ]

    candidate = UMI(
        length=4,
        sequence="AAAA",
    )

    assert minimum_distance_to_codebook(
        candidate,
        codebook,
    ) == 0  

def test_optimise_codebook_returns_requested_size():

    candidates = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
        UMI(length=4, sequence="GGGG"),
        UMI(length=4, sequence="TTTT"),
    ]

    codebook = optimise_codebook(
        candidates,
        size=3,
        seed=42,
    )

    assert len(codebook) == 3

def test_optimise_codebook_selects_existing_candidates():

    candidates = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
        UMI(length=4, sequence="GGGG"),
        UMI(length=4, sequence="TTTT"),
    ]

    codebook = optimise_codebook(
        candidates,
        size=2,
        seed=42,
    )

    candidate_sequences = {
    umi.sequence
    for umi in candidates
}

    selected_sequences = {
        umi.sequence
        for umi in codebook
}

    assert selected_sequences.issubset(candidate_sequences)

def test_optimise_codebook_reproducible_with_seed():

    candidates = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
        UMI(length=4, sequence="GGGG"),
        UMI(length=4, sequence="TTTT"),
    ]

    first = optimise_codebook(
        candidates,
        size=3,
        seed=42,
    )

    second = optimise_codebook(
        candidates,
        size=3,
        seed=42,
    )

    assert first == second

def test_optimise_codebook_rejects_large_size():

    candidates = [
        UMI(length=4, sequence="AAAA"),
        UMI(length=4, sequence="CCCC"),
    ]

    with pytest.raises(ValueError):

        optimise_codebook(
            candidates,
            size=3,
        )
    