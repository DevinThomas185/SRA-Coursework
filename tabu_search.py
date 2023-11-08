from Job import Job
from DirectedAcyclicGraph import DirectedAcyclicGraph
from tabulate import tabulate


# TODO: Needs to account for precedence constraints
def neighbourhood_generator(candidate: list, last_index_swapped: int):
    i = last_index_swapped + 1 if last_index_swapped != len(candidate) - 2 else 0

    while i != last_index_swapped:
        if i == len(candidate) - 2:
            i = 0
        else:
            i += 1

        next_candidate = candidate.copy()
        next_candidate[i], next_candidate[i + 1] = (
            next_candidate[i + 1],
            next_candidate[i],
        )

        yield next_candidate, (next_candidate[i], next_candidate[i + 1]), i - 1

    yield None, None, None


def tabu_search(
    graph: DirectedAcyclicGraph,
    initial_candidate,
    tabu_list_size: int,
    gamma: int,
    iterations: int,
    cost_function: callable,
    verbose: bool = False,
):
    best_candidate = initial_candidate
    best_cost = cost_function(initial_candidate)

    current_candidate = initial_candidate
    current_cost = cost_function(initial_candidate)
    seen_candidates = [initial_candidate.copy()]

    tabu_list = []

    # TODO: Figure out how to do this Tabu flag
    tabu = False

    last_index_swapped = len(initial_candidate) - 2

    table = [
        [0, current_candidate.copy(), current_cost, tabu_list.copy(), best_cost, tabu]
    ]

    for k in range(1, iterations):
        neighbours = neighbourhood_generator(current_candidate, last_index_swapped)
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
            tabu = True if next_candidate in seen_candidates else False

            table.append(
                [k, next_candidate.copy(), next_cost, tabu_list.copy(), best_cost, tabu]
            )

            seen_candidates.append(next_candidate)

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

    return best_candidate, best_cost
