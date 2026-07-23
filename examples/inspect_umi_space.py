"""
Explore the available UMI design space.

Reports:
- uniqueness
- GC distribution
- homopolymer distribution
- fraction surviving biological constraints

This is an exploratory analysis tool,
not part of the production pipeline.
"""

from umicode.design import generate_candidate_umis


def calculate_gc(sequence: str) -> float:
    """
    Calculate GC fraction of a DNA sequence.
    """

    gc_count = sequence.count("G") + sequence.count("C")

    return gc_count / len(sequence)


def maximum_homopolymer_length(sequence: str) -> int:
    """
    Find the longest run of identical bases.
    """

    longest = 1
    current = 1

    for previous, current_base in zip(sequence, sequence[1:]):

        if current_base == previous:
            current += 1
            longest = max(longest, current)

        else:
            current = 1

    return longest

def passes_gc(sequence: str) -> bool:
    gc = calculate_gc(sequence)
    return 0.40 <= gc <= 0.60


def passes_homopolymer(sequence: str) -> bool:
    return maximum_homopolymer_length(sequence) <= 3

def main():

    number = 100000
    length = 16

    umis = generate_candidate_umis(
        number=number,
        length=length,
    )

    sequences = [
        umi.sequence
        for umi in umis
    ]

    print(f"Generated UMIs: {len(sequences)}")
    print(f"UMI length: {length}")

    print(
        f"Unique sequences: {len(set(sequences))}"
    )

    gc_values = [
        calculate_gc(seq)
        for seq in sequences
    ]

    print()
    print("GC content:")
    print(f"  minimum: {min(gc_values):.2f}")
    print(f"  maximum: {max(gc_values):.2f}")
    print(f"  mean:    {sum(gc_values)/len(gc_values):.2f}")

    homopolymers = [
        maximum_homopolymer_length(seq)
        for seq in sequences
    ]

    print()
    print("Homopolymers:")
    print(
        f"  longest observed: {max(homopolymers)}"
    )

    passing = [
        seq
        for seq in sequences
        if passes_gc(seq)
        and passes_homopolymer(seq)
    ]

    print()

    print("Constraint survival:")
    print(
        f"  passing: {len(passing)} / {len(sequences)}"
    )

    survival_fraction = len(passing) / len(sequences)

    print(
        f"  survival: {survival_fraction:.1%}"
    )

if __name__ == "__main__":
    main()
