from dataclasses import dataclass


@dataclass
class AnchorDesign:
    """
    Represents the process of designing an anchor sequence.

    An anchor is a fixed sequence adjacent to the UMI.
    """

    length: int
    selected_sequence: str | None = None


def is_valid_anchor_length(length: int) -> bool:
    """
    Basic sanity check for anchor length.
    """
    return length > 0