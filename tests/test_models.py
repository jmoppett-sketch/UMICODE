from umicode.models import (
    Anchor,
    Spacer,
    UMI,
    CassetteSide,
    CassetteDesign,
)


def test_create_umi():
    umi = UMI(length=16)

    assert umi.length == 16
    assert umi.sequence is None


def test_create_cassette():

    left = CassetteSide(
        anchor=Anchor(sequence=None, length=8),
        spacer=Spacer(sequence="AT"),
        umi=UMI(length=16),
    )

    right = CassetteSide(
        anchor=Anchor(sequence=None, length=8),
        spacer=Spacer(sequence="TA"),
        umi=UMI(length=16),
    )

    cassette = CassetteDesign(
        left=left,
        right=right,
    )

    assert cassette.left.umi.length == 16
    assert cassette.right.umi.length == 16
    assert cassette.left.spacer.sequence == "AT"