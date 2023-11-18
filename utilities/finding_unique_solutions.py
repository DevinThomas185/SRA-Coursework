import math
from itertools import product
import numpy as np


## Code to exhaustively figure out the results of the number of unique solutions for a given schedule length
# ADJACENT SWAPS
def swapper(i, text):
    return text[:i] + text[i + 1] + text[i] + text[i + 2 :]


def compute_adjacent(text):
    i = 1
    seen_permutations = {text}

    total_permutations = math.factorial(len(text))

    found_at_level_i = {0: 1}

    while len(seen_permutations) < total_permutations:
        found = 0
        combinations = list(product(range(len(text) - 1), repeat=i))
        for combination in combinations:
            t = text
            for swap in combination:
                t = swapper(swap, t)

            if t not in seen_permutations:
                seen_permutations.add(t)
                found += 1

        found_at_level_i[i] = found

        i += 1
        print(i, found_at_level_i.values(), len(seen_permutations) / total_permutations)

    print(found_at_level_i)
    print(found_at_level_i.values())
    print(sum(found_at_level_i.values()))
    print(sum(found_at_level_i.values()) == len(seen_permutations))


## Returns the number of unique permutations found for a schedule of length l
def get_unique_solutions_after_x_adjacent_swaps(l):
    if l == 1:
        return [1]

    prev = get_unique_solutions_after_x_adjacent_swaps(l - 1)
    size = len(prev) + l - 1
    res = np.zeros(size)

    for i in range(size):
        res[i] = res[i - 1]
        if i < len(prev):
            res[i] += prev[i]
        if i >= l:
            res[i] -= prev[i - l]

    return res


## Code to exhaustively figure out the results of the number of unique solutions for a given schedule length
# RANDOM SWAPS
def swapper_i_j(i, j, text):
    x = list(text)
    x[i], x[j] = x[j], x[i]
    return "".join(x)


def compute_all(text):
    seen_permutations = {text}

    total_permutations = math.factorial(len(text))

    found_at_level_i = {0: 1}

    i = 1
    possible_pairs_to_swap = list(product(range(len(text)), repeat=2))
    while len(seen_permutations) < total_permutations:
        found = 0
        combinations = list(product(possible_pairs_to_swap, repeat=i))
        for combination in combinations:
            t = text
            for k, j in combination:
                t = swapper_i_j(k, j, t)

            if t not in seen_permutations:
                seen_permutations.add(t)
                found += 1

        found_at_level_i[i] = found

        i += 1
        print(i, len(seen_permutations) / total_permutations)

    print(found_at_level_i)
    print(found_at_level_i.values())
    print(sum(found_at_level_i.values()))
    print(sum(found_at_level_i.values()) == len(seen_permutations))


# Stirling numbers
def get_unique_solutions_after_x_random_swaps(l):
    stirling_numbers = np.zeros((l + 1, l + 1))

    stirling_numbers[0, 0] = 1

    for n in range(1, l + 1):
        for k in range(1, n + 1):
            stirling_numbers[n, k] = (
                stirling_numbers[n - 1, k - 1] + (n - 1) * stirling_numbers[n - 1, k]
            )

    return stirling_numbers[l, :][::-1][:-1]
