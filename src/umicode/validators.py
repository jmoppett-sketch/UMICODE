from .models import Anchor, UMI, CassetteDesign


DNA_BASES = {"A", "C", "G", "T"}


def validate_sequence(sequence: str) -> bool:
    """
    Check that a sequence contains valid DNA bases.
    """
    return set(sequence.upper()).issubset(DNA_BASES)


def validate_anchor(anchor: Anchor) -> bool:
    """
    Check anchor length and sequence if provided.
    """

    if anchor.length <= 0:
        return False

    if anchor.sequence is not None:
        if len(anchor.sequence) != anchor.length:
            return False

        if not validate_sequence(anchor.sequence):
            return False

    return True


def validate_umi(umi: UMI) -> bool:
    """
    Basic UMI validation.
    """

    if umi.length <= 0:
        return False

    if umi.sequence is not None:
        if len(umi.sequence) != umi.length:
            return False

        if not validate_sequence(umi.sequence):
            return False

    return True


def validate_cassette(cassette: CassetteDesign) -> bool:
    """
    Validate both sides of the cassette.
    """

    return (
        validate_anchor(cassette.left.anchor)
        and validate_anchor(cassette.right.anchor)
        and validate_umi(cassette.left.umi)
        and validate_umi(cassette.right.umi)
    )

def validate_generation_parameters(
    number: int,
    length: int,
) -> None:
    """
    Validate parameters used for candidate UMI generation.

    Raises
    ------
    ValueError
        If number or length are invalid.
    """

    if number <= 0:
        raise ValueError(
            f"Number of candidate UMIs must be greater than zero (received {number})."
        )

    if length <= 0:
        raise ValueError(
            f"UMI length must be greater than zero (received {length})."
        )