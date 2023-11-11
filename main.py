import numpy as np
import matplotlib.pyplot as plt

from tabu_search import tabu_search
from cost_functions import sum_tardiness, sum_weighted_tardiness
from utilities import print_schedule, format_number, print_schedule_to_csv

from CourseworkProblem import CourseworkProblem
from ClassProblems import ClassProblem1, ClassProblem2


def run_tabu_search_on_class_problem_1(
    gamma: int = 20,
    iterations: int = 4,
    tabu_list_size: int = 2,
    strict_tabu_tenure: bool = False,
    verbose: bool = True,
):
    problem = ClassProblem1()
    schedule, cost = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_weighted_tardiness,
        strict_tabu_tenure=strict_tabu_tenure,
        verbose=verbose,
    )
    return schedule, cost


def run_tabu_search_on_class_problem_2(
    gamma: int = 100,
    iterations: int = 3,
    tabu_list_size: int = 2,
    verbose: bool = True,
):
    problem = ClassProblem2()
    schedule, cost = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_weighted_tardiness,
        verbose=verbose,
    )
    return schedule, cost


def run_tabu_search_on_coursework_problem(
    gamma: int = 10,
    iterations: int = 100_000,
    tabu_list_size: int = 20,
    verbose: bool = False,
):
    problem = CourseworkProblem()
    problem.get_graph().print_graph()
    schedule, cost = tabu_search(
        problem=problem,
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_tardiness,
        verbose=verbose,
    )
    return schedule, cost


def plot_changing_gamma():
    gammas = np.arange(1, 101, 1)
    costs = []
    for gamma in gammas:
        _, cost = run_tabu_search_on_coursework_problem(
            gamma=gamma,
            iterations=10_000,
        )
        costs.append(cost)

    # Plot
    plt.plot(gammas, costs)
    plt.xlabel("Gamma")
    plt.xticks(gammas[::5])
    plt.ylabel("Cost")
    plt.title("Optimal Cost as Gamma Changes")
    plt.show()


def plot_changing_tabu_list_size():
    tabu_list_sizes = np.arange(1, 101, 1)
    costs = []

    for tabu_list_size in tabu_list_sizes:
        _, cost = run_tabu_search_on_coursework_problem(
            iterations=10_000,
            tabu_list_size=tabu_list_size,
        )
        costs.append(cost)

    # Plot
    plt.plot(tabu_list_sizes, costs)
    plt.xlabel("Tabu List Size")
    plt.xticks(tabu_list_sizes[::5])
    plt.ylabel("Cost")
    plt.title("Optimal Cost as Tabu List Size Changes")
    plt.show()


def main():
    # schedule, cost = run_tabu_search_on_class_problem_1()
    # schedule, cost = run_tabu_search_on_class_problem_2()
    schedule, cost = run_tabu_search_on_coursework_problem(
        gamma=10,
        iterations=10,
        tabu_list_size=20,
        verbose=False,
    )
    print(schedule, cost)
    # print_schedule_to_csv(schedule, "sinit")

    # plot_changing_gamma()
    # plot_changing_tabu_list_size()




if __name__ == "__main__":
    main()




