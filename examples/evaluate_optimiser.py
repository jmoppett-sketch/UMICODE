"""
Compare random and optimised UMI codebooks.
"""

import random
import statistics
import time


from umicode.design import generate_candidate_umis
from umicode.optimisation import optimise_codebook
from umicode.scoring import (
    mean_pairwise_distance,
    minimum_pairwise_distance,
)


def main():

    candidate_number = 5000
    umi_length = 16
    codebook_size = 96

    verbose = False

    start = time.perf_counter()

    random_minima = []
    optimised_minima = []

    random_means = []
    optimised_means = []

    for seed in range(10):

        candidates = generate_candidate_umis(
            number=candidate_number,
            length=umi_length,
        )
        rng = random.Random(seed)

        random_codebook = rng.sample(
            candidates,
            codebook_size,
        )
        optimised_codebook = optimise_codebook(
            candidates,
            size=codebook_size,
            seed=seed,
        )

        if verbose:

            print()
            print(f"Seed {seed}")
            for umi in optimised_codebook[:5]:
                print(umi.sequence)

        random_minimum = minimum_pairwise_distance(
            random_codebook,
        )

        random_mean = mean_pairwise_distance(
            random_codebook,
        )

        optimised_minimum = minimum_pairwise_distance(
            optimised_codebook,
        )

        optimised_mean = mean_pairwise_distance(
            optimised_codebook,
        )
        random_minima.append(random_minimum)
        optimised_minima.append(optimised_minimum)

        random_means.append(random_mean)
        optimised_means.append(optimised_mean)

    print()
    print("Summary over 10 runs")
    print("====================")

    print()
    print("Random minimum distance")
    print("-----------------------")
    print(f"Values: {random_minima}")
    print(f"Mean:   {statistics.mean(random_minima):.2f}")
    print(f"SD:     {statistics.stdev(random_minima):.2f}")
    print(f"Min:    {min(random_minima)}")
    print(f"Max:    {max(random_minima)}")

    print()

    print("Optimised minimum distance")
    print("--------------------------")
    print(f"Values: {optimised_minima}")
    print(f"Mean:   {statistics.mean(optimised_minima):.2f}")
    print(f"SD:     {statistics.stdev(optimised_minima):.2f}")
    print(f"Min:    {min(optimised_minima)}")
    print(f"Max:    {max(optimised_minima)}")

    print()
    print("Mean pairwise distance")
    print("----------------------")

    print("Random")
    print(f"Mean: {statistics.mean(random_means):.2f}")
    print(f"SD:   {statistics.stdev(random_means):.2f}")

    print()

    print("Optimised")
    print(f"Mean: {statistics.mean(optimised_means):.2f}")
    print(f"SD:   {statistics.stdev(optimised_means):.2f}")

    elapsed = time.perf_counter() - start

    print()
    print(f"Elapsed time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    main()
