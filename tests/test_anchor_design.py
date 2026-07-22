from umicode.anchor_design import (
    AnchorDesign,
    is_valid_anchor_length,
)


def test_anchor_design():

    anchor = AnchorDesign(
        length=8
    )

    assert anchor.length == 8
    assert anchor.selected_sequence is None


def test_anchor_length():

    assert is_valid_anchor_length(8)
    assert not is_valid_anchor_length(0)