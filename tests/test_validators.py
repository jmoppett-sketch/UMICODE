from umicode.models import Anchor, UMI, Spacer, CassetteSide, CassetteDesign
from umicode.validators import (
    validate_sequence,
    validate_anchor,
    validate_umi,
    validate_cassette,
)


def test_valid_dna_sequence():
    assert validate_sequence("ATCG")


def test_invalid_dna_sequence():
    assert not validate_sequence("ATCX")


def test_valid_anchor():

    anchor = Anchor(
        sequence="ATCGATCG",
        length=8,
    )

    assert validate_anchor(anchor)


def test_invalid_umi_length():

    umi = UMI(
        sequence="ATCG",
        length=8,
    )

    assert not validate_umi(umi)


def test_valid_cassette():

    left = CassetteSide(
        anchor=Anchor(None, 8),
        spacer=Spacer("AT"),
        umi=UMI(16),
    )

    right = CassetteSide(
        anchor=Anchor(None, 8),
        spacer=Spacer("TA"),
        umi=UMI(16),
    )

    cassette = CassetteDesign(
        left=left,
        right=right,
    )

    assert validate_cassette(cassette)