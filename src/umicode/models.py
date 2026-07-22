from dataclasses import dataclass


@dataclass
class Anchor:
    """
    Represents the fixed sequence region adjacent to the UMI.

    The sequence may be unknown during early design stages.
    """
    sequence: str | None
    length: int


@dataclass
class Spacer:
    """
    Represents a fixed spacer sequence between anchor and UMI.
    """
    sequence: str


@dataclass
class UMI:
    """
    Represents a molecular identifier.

    The sequence is optional because initially we are
    designing the codebook rather than representing a read.
    """
    length: int
    sequence: str | None = None


@dataclass
class CassetteSide:
    """
    Represents one side of the capture cassette.

    Structure:
    adapter -> anchor -> spacer -> UMI
    """
    anchor: Anchor
    spacer: Spacer
    umi: UMI


@dataclass
class CassetteDesign:
    """
    Complete duplex UMI cassette design.

    Structure:

    LEFT UMI -- insert -- RIGHT UMI
    """
    left: CassetteSide
    right: CassetteSide