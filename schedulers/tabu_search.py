from classes.Problem import Problem
from tabulate import tabulate

from utilities.utilities import format_number, print_execution_to_file


def neighbourhood_generator(
    problem: Problem,
    candidate: list,
    last_index_swapped: int,
    strict_tabu_tenure: bool = False,
):
    i = (
        last_index_swapped + 1
        if last_index_swapped != problem.get_schedule_size() - 2
        else 0
    )

    while True:
        next_candidate = candidate.copy()

        job1 = next_candidate[i]
        job2 = next_candidate[i + 1]

        next_candidate[i] = job2
        next_candidate[i + 1] = job1

        # Check if the swap is valid against precedences, then yield candidate
        if (
            problem.get_graph().get_transitive_closure()[
                job1.get_id() - 1, job2.get_id() - 1
            ]
            == 0
        ):
            # If strict, we ensure that no swaps involving two jobs can be done, if they are already in the Tabu List
            # The ordering ensures that they will clash with the Tabu List since that entry will also be ordered
            if strict_tabu_tenure:
                if job1.get_id() > job2.get_id():
                    job1, job2 = job2, job1

            yield next_candidate, (job1, job2), i

        i = 0 if i == len(candidate) - 2 else i + 1

        if i == last_index_swapped + 1:
            break

    yield None, None, None


def tabu_search(
    problem: Problem,
    tabu_list_size: int,
    gamma: int,
    iterations: int,
    cost_function: callable,
    strict_tabu_tenure: bool = False,
    verbose: bool = False,
    print_file: str = None,
):
    initial_candidate = problem.get_initial_candidate()

    next_candidate = initial_candidate
    next_cost = cost_function(next_candidate)

    best_candidate = initial_candidate
    best_cost = cost_function(best_candidate)
    best_costs = [best_cost]

    current_candidate = initial_candidate
    current_cost = cost_function(initial_candidate)
    seen_candidates = [initial_candidate.copy()]

    tabu_list = []

    # TODO: Figure out how to do this Tabu flag
    tabu = False

    last_index_swapped = problem.get_schedule_size() - 2

    table = [
        [
            0,
            current_candidate.copy(),
            current_cost,
            tabu_list.copy(),
            best_cost,
            tabu,
        ]
    ]

    for k in range(1, iterations + 1):
        best_costs.append(best_cost)
        if verbose and k % 1_000 == 0:
            print(f"Iteration {format_number(k)}")

        if next_candidate == None:
            if verbose:
                print(f"Local minimum found at iteration {format_number(k)}")
            break

        neighbours = neighbourhood_generator(
            problem, current_candidate, last_index_swapped, strict_tabu_tenure
        )

        while True:
            next_candidate, swapped_jobs, last_index_swapped = next(neighbours)

            # No more candidates left to check
            if next_candidate is None:
                break

            next_cost = cost_function(next_candidate)
            delta = current_cost - next_cost

            # Append row to Tabu Search table
            if verbose or print_file is not None:
                # Only track seen candidates if we are printing, since it is needed for the Tabu flag
                tabu = True if next_candidate in seen_candidates else False
                seen_candidates.append(next_candidate)

                table.append(
                    [
                        k,
                        next_candidate.copy(),
                        next_cost,
                        tabu_list.copy(),
                        best_cost,
                        tabu,
                    ]
                )

            # Move to next iteration if meets aspiration criteria or is better than current best
            if (
                delta > -gamma and swapped_jobs not in tabu_list
            ) or next_cost < best_cost:
                break

        # Update best candidate if necessary
        if next_cost < best_cost:
            best_candidate = next_candidate
            best_cost = next_cost

        current_candidate = next_candidate
        current_cost = next_cost

        # Append (i, j) to tabu list
        tabu_list.append(swapped_jobs)

        # Remove oldest pair from tabu list if it exceeds the maximum size
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

    print_table = tabulate(
        table,
        headers=[
            "Iteration",
            "Candidate",
            "Cost",
            "Tabu List",
            "Best Cost",
            "Tabu?",
        ],
    )

    if verbose:
        print()
        print(print_table)
        print(f"Best Schedule {best_candidate} with cost {best_cost}")

    if print_file is not None:
        params = {
            "Problem": problem.get_problem_name(),
            "Tabu List Size": tabu_list_size,
            "γ": gamma,
            "Iterations": iterations,
            "Cost Function": cost_function.__name__,
            "Strict Tabu Tenure": strict_tabu_tenure,
        }
        print_execution_to_file(
            print_file, print_table, best_candidate, best_cost, params
        )

    return best_candidate, best_cost, best_costs
