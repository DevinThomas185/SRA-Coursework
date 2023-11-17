from Problem import Problem
from tabulate import tabulate
import numpy as np
from utilities import format_number


def check_schedule_validity(we_have: np.ndarray, problem: Problem):
    diff = we_have - problem.get_graph().get_transitive_closure()
    return np.all(diff >= 0)


def generate_schedule_transitive_closure(schedule: list, problem: Problem):
    we_have = np.zeros(problem.get_graph().get_incidence_matrix().shape)

    for i in range(len(schedule) - 1):
        for j in range(i + 1, len(schedule)):
            we_have[schedule[i].get_id() - 1, schedule[j].get_id() - 1] = 1

    return we_have


def swap_rows_and_columns(s_tc: np.ndarray, job_1_id: int , job_2_id: int):
    index1 = job_1_id - 1
    index2 = job_2_id - 1

    s_tc[[index1, index2], :] = s_tc[[index2, index1], :]
    s_tc[:, [index1, index2]] = s_tc[:, [index2, index1]]

    return s_tc


def select_random_candidate_from_neighbourhood_i(
    candidate: list,
    i: int,
    problem: Problem,
):
    if i != 1:
        i = np.random.choice([i, i - 1], 1, p=[0.5, 0.5])[0]

    next_candidate = candidate.copy()
    schedule_tc = generate_schedule_transitive_closure(candidate, problem)

    while next_candidate == candidate:
        next_candidate = candidate.copy()
        current_schedule_tc = schedule_tc.copy()

        # Complete i random swaps
        for _ in range(i):
            [index1, index2] = sorted(
                np.random.choice(range(0, len(candidate) - 1), 2, replace=False)
            )

            job_1 = next_candidate[index1]
            job_2 = next_candidate[index2]

            # Swap jobs at index 1 and 2
            next_candidate[index1] = job_2
            next_candidate[index2] = job_1

            # Swap columns and rows of the schedule transitive closure at index 1 and 2
            current_schedule_tc = swap_rows_and_columns(
                current_schedule_tc, job_1.get_id(), job_2.get_id()
            )

            # If the resulting schedule is invalid, undo the swap
            if not check_schedule_validity(current_schedule_tc, problem):
                next_candidate[index1] = job_1
                next_candidate[index2] = job_2

                # Undo swap of jobs in transitive closure of the schedule
                current_schedule_tc = swap_rows_and_columns(
                    current_schedule_tc, job_1.get_id(), job_2.get_id()
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
        if verbose and k % 1 == 0:
            print(f"Iteration {format_number(k)}")

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
                # print(current_cost, next_cost, delta)
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
