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
    schedule, cost, best_costs = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_weighted_tardiness,
        strict_tabu_tenure=strict_tabu_tenure,
        verbose=verbose,
    )
    return schedule, cost, best_costs


def run_tabu_search_on_class_problem_2(
    gamma: int = 100,
    iterations: int = 3,
    tabu_list_size: int = 2,
    verbose: bool = True,
):
    problem = ClassProblem2()
    schedule, cost, best_costs = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_weighted_tardiness,
        verbose=verbose,
    )
    return schedule, cost, best_costs


def run_tabu_search_on_coursework_problem(
    gamma: int = 10,
    iterations: int = 100_000,
    tabu_list_size: int = 20,
    verbose: bool = False,
):
    problem = CourseworkProblem()
    schedule, cost, best_costs = tabu_search(
        problem=problem,
        tabu_list_size=tabu_list_size,
        gamma=gamma,
        iterations=iterations,
        cost_function=sum_tardiness,
        verbose=verbose,
    )
    return schedule, cost, best_costs


def plot_changing_gamma(iterations: int = 100_000, min_gamma=1, max_gamma=101, step_gamma=5):
    gammas = np.arange(min_gamma, max_gamma, step_gamma)
    costs = []
    best_costs_per_gamma = {}
    for gamma in gammas:
        _, cost, best_costs = run_tabu_search_on_coursework_problem(
            gamma=gamma,
            iterations=iterations,
        )
        costs.append(cost)
        best_costs_per_gamma[gamma] = best_costs

    # Plot
    plt.plot(gammas, costs)
    plt.xlabel("γ")
    plt.xticks(gammas[::5])
    plt.ylabel("Cost")
    plt.title(f"Optimal Cost after K={format_number(iterations)} Iterations with varying γ")
    plt.show()

    for gamma, bc in best_costs_per_gamma.items():
        plt.plot(np.arange(iterations + 1), bc, label=f"γ={gamma}")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.title(f"Best cost per iteration with different γ")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()
    


def plot_changing_tabu_list_size(iterations: int = 100_000, min_L=1 max_L=101, step_L=5):
    tabu_list_sizes = np.arange(min_L, max_L, step_L)
    costs = []
    best_costs_per_tabu_list_size = {}
    for tabu_list_size in tabu_list_sizes:
        _, cost, best_costs = run_tabu_search_on_coursework_problem(
            iterations=iterations,
            tabu_list_size=tabu_list_size,
        )
        costs.append(cost)
        best_costs_per_tabu_list_size[tabu_list_size] = best_costs

    # Plot
    plt.plot(tabu_list_sizes, costs)
    plt.xlabel("Tabu List Size")
    plt.xticks(tabu_list_sizes[::5])
    plt.ylabel("Cost")
    plt.title(f"Optimal Cost after K={format_number(iterations)} Iterations with varying Tabu List Size")
    plt.show()

    for tabu_list_size, bc in best_costs_per_tabu_list_size.items():
        plt.plot(np.arange(iterations + 1), bc, label=f"L={tabu_list_size}")
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.title(f"Best cost per iteration with different Tabu List Size")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.show()


def main():
    # schedule, cost, _ = run_tabu_search_on_class_problem_1()
    # schedule, cost, _ = run_tabu_search_on_class_problem_2()
    # schedule, cost, _ = run_tabu_search_on_coursework_problem(
    #     gamma=10,
    #     iterations=10,
    #     tabu_list_size=20,
    #     verbose=False,
    # )
    # print(schedule, cost)
    # print_schedule_to_csv(schedule, "sinit")

    test_iterations = 10_000
    min_gamma = 1
    max_gamma = 101
    step_gamma = 5
    plot_changing_gamma(test_iterations)
    
    min_L = 1
    max_L = 101
    step_L = 5
    plot_changing_tabu_list_size(test_iterations)




if __name__ == "__main__":
    main()




