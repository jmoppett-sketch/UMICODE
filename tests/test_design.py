from umicode.design import generate_candidate_umis


def test_generate_candidate_umis_returns_correct_number():

    umis = generate_candidate_umis(
        number=10,
        length=16,
    )

    assert len(umis) == 10

def test_generated_umis_have_correct_length():

    umis = generate_candidate_umis(
        number=5,
        length=12,
    )

    for umi in umis:
        assert len(umi.sequence) == 12

def test_generated_umis_contain_only_dna():

    umis = generate_candidate_umis(
        number=20,
        length=16,
    )

    for umi in umis:
        assert set(umi.sequence) <= {"A", "C", "G", "T"}