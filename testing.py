import math
from itertools import product
import numpy as np


def swapper(i, text):
    return text[:i] + text[i + 1] + text[i] + text[i + 2 :]


def compute(text):
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

# Returns the number of unique permutations found 
def get_level(level):
    if level == 1:
        return [1]

    prev = get_level(level - 1)
    size = len(prev) + level - 1
    res = np.zeros(size)

    for i in range(size):
        res[i] = res[i - 1]
        if i < len(prev):
            res[i] += prev[i]
        if i >= level:
            res[i] -= prev[i - level]

    return res
