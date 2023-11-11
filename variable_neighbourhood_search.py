from Problem import Problem
from tabulate import tabulate
import numpy as np


def select_random_candidate_from_neighbourhood_i(
    candidate: list,
    i: int,
    problem: Problem,
):
    next_candidate = candidate.copy()

    while next_candidate == candidate:
        # Complete i random swaps
        for _ in range(i):
            index = np.random.randint(0, len(candidate) - 1)

            job_1 = candidate[index]
            job_2 = candidate[index + 1]

            # Check if the candidate is invalid, if so, try again
            # If we can't do a swap, then the candidate falls into a neighbourhood smaller than i
            if (
                problem.get_graph().get_transitive_closure()[
                    job_1.get_id() - 1, job_2.get_id() - 1
                ]
                == 1
            ):
                continue

            # Otherwise, swap and return
            next_candidate[index], next_candidate[index + 1] = (
                next_candidate[index + 1],
                next_candidate[index],
            )

    return next_candidate


def variable_neighbourhood_search(
    problem: Problem,
    cost_function: callable,
    iterations: int,
    I: int,
    verbose: bool = False,
):
    initial_candidate = problem.get_initial_candidate()

    current_candidate = initial_candidate
    current_cost = cost_function(current_candidate)

    next_candidate = initial_candidate
    next_cost = cost_function(next_candidate)

    table = [[0, 0, current_candidate.copy(), current_cost, current_cost]]

    for k in range(1, iterations):
        if verbose and k % 1000 == 0:
            print(f"Iteration {k}")

        for i in range(1, I):
            if next_candidate is None:
                break

            next_candidate = select_random_candidate_from_neighbourhood_i(
                candidate=current_candidate,
                i=i,
                problem=problem,
            )

            next_cost = cost_function(next_candidate)

            if verbose:
                table.append([k, i, next_candidate.copy(), next_cost, current_cost])

            delta = current_cost - next_cost

            if delta > 0:
                current_candidate = next_candidate
                current_cost = next_cost
                break

    if verbose:
        print(
            tabulate(
                table,
                headers=[
                    "Iteration",
                    "Ni",
                    "Candidate",
                    "Cost",
                    "Best Cost",
                ],
            )
        )
        print(f"Best candidate: {current_candidate}")
        print(f"Best cost: {current_cost}")

    return current_candidate, current_cost
