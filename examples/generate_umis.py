from umicode.design import generate_candidate_umis

umis = generate_candidate_umis(
    number=10,
    length=16,
)

for umi in umis:
    print(umi)
    