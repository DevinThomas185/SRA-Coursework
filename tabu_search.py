from DirectedAcyclicGraph import DirectedAcyclicGraph
from Problem import Problem
from tabulate import tabulate

from utilities import format_number


# TODO: Needs to account for precedence constraints
def neighbourhood_generator(
    candidate: list, last_index_swapped: int, graph: DirectedAcyclicGraph
):
    i = last_index_swapped + 1 if last_index_swapped != len(candidate) - 2 else 0

    while True:
        next_candidate = candidate.copy()
        next_candidate[i], next_candidate[i + 1] = (
            next_candidate[i + 1],
            next_candidate[i],
        )

        # Check if the swap is valid, then yield candidate
        if (
            graph.get_transitive_closure()[
                next_candidate[i + 1].get_id() - 1, next_candidate[i].get_id() - 1
            ]
            == 0
        ):
            yield next_candidate, (next_candidate[i], next_candidate[i + 1]), i


        i = 0 if i == len(candidate) - 2 else i+1

        if i == last_index_swapped+1:
            break

    yield None, None, None


def tabu_search(
    problem: Problem,
    tabu_list_size: int,
    gamma: int,
    iterations: int,
    cost_function: callable,
    verbose: bool = False,
):
    graph = problem.get_graph()
    initial_candidate = problem.get_initial_candidate()

    best_candidate = initial_candidate
    best_cost = cost_function(initial_candidate)

    current_candidate = initial_candidate
    current_cost = cost_function(initial_candidate)
    seen_candidates = [initial_candidate.copy()]

    tabu_list = []

    # TODO: Figure out how to do this Tabu flag
    tabu = False

    last_index_swapped = len(initial_candidate) - 2

    if verbose:
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

    # Compute transitive closure for neighbourhood generation ensuring no candidates
    # are generated that violate precedence constraints
    graph.compute_transitive_closure()

    for k in range(1, iterations + 1):
        if verbose and k % 1_000 == 0:
            print(f"Iteration {format_number(k)}")

        neighbours = neighbourhood_generator(
            current_candidate, last_index_swapped, graph
        )

        while True:
            next_candidate, swapped_jobs, last_index_swapped = next(neighbours)

            # No more candidates left to check
            if next_candidate is None:
                break

            next_cost = cost_function(next_candidate)
            delta = current_cost - next_cost

            # Update best candidate if necessary
            if next_cost < best_cost:
                best_candidate = next_candidate
                best_cost = next_cost

            # Append row to Tabu Search table
            if verbose:
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

        current_candidate = next_candidate
        current_cost = next_cost

        # Append (i, j) to tabu list
        tabu_list.append(swapped_jobs)

        # Remove oldest pair from tabu list if it exceeds the maximum size
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

    if verbose:
        print()
        print(
            tabulate(
                table,
                headers=[
                    "Solution",
                    "Candidate",
                    "Cost",
                    "Tabu List",
                    "Best Cost",
                    "Tabu?",
                ],
            )
        )
        print(f"Best Schedule {best_candidate} with cost {best_cost}")

    return best_candidate, best_cost
