from Job import Job
from DirectedAcyclicGraph import DirectedAcyclicGraph
from tabulate import tabulate


def variable_neighbourhood_search(
    graph: DirectedAcyclicGraph,
    initial_candidate,
    cost_function: callable,
    tabu_list_size: int,
    iterations: int,
    neighbourhood_generation_functions: list,
    verbose: bool = False,
):
    current_candidate = initial_candidate
    current_cost = cost_function(initial_candidate)

    table = [0, 0, current_candidate.copy(), current_cost, current_cost]

    for k in range(1, iterations):
        for i in range(len(neighbourhood_generation_functions)):

            table.append([k, i, current_candidate.copy(), current_cost, current_cost])

            next_candidate = neighbourhood_generation_functions[i](...) # Select neighbour using neighbourhood function
            next_cost = cost_function(next_candidate)

            delta = current_cost - next_cost

            if delta > 0:
                current_candidate = next_candidate
                current_cost = next_cost
                break

    print(tabulate(table, headers=["Iteration", "Neighbourhood Function", "Candidate", "Cost"]))
