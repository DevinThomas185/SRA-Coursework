from Job import Job
from DirectedAcyclicGraph import DirectedAcyclicGraph
from tabulate import tabulate


def select_neighbour_from_neighbourhood(candidate: list, next_index_to_swap: int):
    # Select the next pair of jobs to swap
    i, j = next_index_to_swap, next_index_to_swap + 1

    # Swap the jobs
    next_candidate = candidate.copy()
    swapped_jobs = (next_candidate[i], next_candidate[j])
    next_candidate[i], next_candidate[j] = next_candidate[j], next_candidate[i]

    if next_index_to_swap == len(candidate) - 2:
        next_index_to_swap = 0
    else:
        next_index_to_swap += 1

    # TODO: Does the order of the swapped jobs need to sorted (to check if already in Tabu List)

    return next_candidate, swapped_jobs, next_index_to_swap


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

    tabu_list = []
    
    # TODO: Figure out how to do this Tabu flag
    tabu = False

    i, j = 0, 0
    next_index_to_swap = 0

    table = [[0, current_candidate.copy(), current_cost, tabu_list.copy(), best_cost, tabu]]

    for k in range(1, iterations):
        while True:

            (
                next_candidate,
                swapped_jobs,
                next_index_to_swap,
            ) = select_neighbour_from_neighbourhood(
                current_candidate, next_index_to_swap
            )

            next_cost = cost_function(next_candidate)

            table.append([k, next_candidate.copy(), next_cost, tabu_list.copy(), best_cost, tabu])
            
            delta = current_cost - next_cost

            if delta > -gamma and swapped_jobs not in tabu_list:
                tabu = True
                break

            if next_cost < best_cost:
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
    

    if verbose:
        print(
            tabulate(
                table,
                headers=[
                    "Solution",
                    "Candidates",
                    "Cost",
                    "Tabu List",
                    "Best Cost",
                    "Tabu?",
                ],
            )
        )

    return best_candidate, best_cost
