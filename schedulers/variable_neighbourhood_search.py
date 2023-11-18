from classes.Problem import Problem
from tabulate import tabulate
import numpy as np
from utilities.utilities import format_number, print_execution_to_file

from utilities.finding_unique_solutions import (
    get_unique_solutions_after_x_adjacent_swaps,
    get_unique_solutions_after_x_random_swaps,
)
from schedulers.tabu_search import tabu_search


def check_schedule_validity(we_have: np.ndarray, problem: Problem):
    diff = we_have - problem.get_graph().get_transitive_closure()
    return np.all(diff >= 0)


def generate_schedule_transitive_closure(schedule: list, problem: Problem):
    we_have = np.zeros(problem.get_graph().get_incidence_matrix().shape)

    for i in range(len(schedule) - 1):
        for j in range(i + 1, len(schedule)):
            we_have[schedule[i].get_id() - 1, schedule[j].get_id() - 1] = 1

    return we_have


def swap_rows_and_columns(s_tc: np.ndarray, job_1_id: int, job_2_id: int):
    index1 = job_1_id - 1
    index2 = job_2_id - 1

    s_tc[[index1, index2], :] = s_tc[[index2, index1], :]
    s_tc[:, [index1, index2]] = s_tc[:, [index2, index1]]

    return s_tc


def select_random_candidate_from_neighbourhood_i(
    candidate: list,
    i: int,
    problem: Problem,
    schedule_tc: np.ndarray,
    unique_solutions_after_x_swaps: list,
    apply_tabu_search: bool = False,
    cost_function: callable = None,
):
    swaps_to_complete = i
    if i != 1:
        # Create two sums of the even and odd indexes of the unique_solutions_after_x_swaps
        even_sum = 0
        odd_sum = 0

        for j in range(0, min(i, len(unique_solutions_after_x_swaps))):
            if j % 2 == 0:
                even_sum += unique_solutions_after_x_swaps[j]
            else:
                odd_sum += unique_solutions_after_x_swaps[j]

        p_i = even_sum if i % 2 == 0 else odd_sum
        p_i = p_i / (even_sum + odd_sum)
        p_i_1 = 1 - p_i

        swaps_to_complete = np.random.choice([i, i - 1], 1, p=[p_i, p_i_1])[0]

    next_candidate = candidate.copy()

    # Continue to generate new candidates until a new candidate is created
    while next_candidate == candidate:
        next_candidate = candidate.copy()
        current_schedule_tc = schedule_tc.copy()

        # Complete random swaps
        swaps_completed = 0
        while swaps_completed < swaps_to_complete:
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
                continue

            swaps_completed += 1

    # Apply Tabu Search to this next candidate
    if apply_tabu_search:
        problem.set_initial_candidate(next_candidate)
        next_candidate, _, _ = tabu_search(
            problem=problem,
            tabu_list_size=2,
            gamma=20,
            iterations=100,
            cost_function=cost_function,
        )
        current_schedule_tc = generate_schedule_transitive_closure(
            next_candidate, problem
        )

    return next_candidate, current_schedule_tc


def variable_neighbourhood_search(
    problem: Problem,
    cost_function: callable,
    iterations: int,
    I: int,
    verbose: bool = False,
    print_file: str = None,
    apply_tabu_search: bool = False,
):
    initial_candidate = problem.get_initial_candidate()

    unique_solutions_after_x_swaps = get_unique_solutions_after_x_random_swaps(
        len(initial_candidate)
    )

    current_candidate = initial_candidate
    current_cost = cost_function(current_candidate)
    current_candidate_tc = generate_schedule_transitive_closure(
        current_candidate, problem
    )

    next_candidate = initial_candidate
    next_cost = cost_function(next_candidate)
    next_candidate_tc = generate_schedule_transitive_closure(next_candidate, problem)

    best_costs = [current_cost]

    table = [[0, 0, current_candidate.copy(), current_cost, current_cost]]

    for k in range(1, iterations + 1):
        best_costs.append(current_cost)
        if verbose and k % 1000 == 0:
            print(f"Iteration {format_number(k)}")

        for i in range(1, I):
            if next_candidate is None:
                break

            (
                next_candidate,
                next_candidate_tc,
            ) = select_random_candidate_from_neighbourhood_i(
                candidate=current_candidate,
                i=i,
                problem=problem,
                schedule_tc=current_candidate_tc,
                unique_solutions_after_x_swaps=unique_solutions_after_x_swaps,
                apply_tabu_search=apply_tabu_search,
                cost_function=cost_function,
            )

            next_cost = cost_function(next_candidate)

            if verbose or print_file is not None:
                table.append([k, i, next_candidate.copy(), next_cost, current_cost])

            delta = current_cost - next_cost

            if delta > 0:
                # print(current_cost, next_cost, delta)
                current_candidate = next_candidate
                current_cost = next_cost
                current_candidate_tc = next_candidate_tc
                break

    print_table = tabulate(
        table,
        headers=[
            "Iteration",
            "Ni",
            "Candidate",
            "Cost",
            "Best Cost",
        ],
    )
    if verbose:
        print(print_table)
        print(f"Best candidate: {current_candidate}")
        print(f"Best cost: {current_cost}")

    if print_file is not None:
        params = {
            "Problem": problem.get_problem_name(),
            "Iterations": iterations,
            "I": I,
            "Cost Function": cost_function.__name__,
        }
        print_execution_to_file(
            print_file, print_table, current_candidate, current_cost, params
        )

    return current_candidate, current_cost, best_costs
