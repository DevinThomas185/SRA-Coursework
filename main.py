from tabu_search import tabu_search
from cost_functions import sum_tardiness, sum_weighted_tardiness
from utilities import print_schedule, format_number

from CourseworkProblem import CourseworkProblem
from ClassProblems import ClassProblem1, ClassProblem2

def main():
    problem = CourseworkProblem()
    # problem.get_graph().print_graph()
    iterations = 100_000
    schedule, cost = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=20,
        gamma=10,
        iterations=iterations,
        cost_function=sum_tardiness,
        verbose=False,
    )
    print_schedule(f"Optimal Schedule for K={format_number(iterations)} (Cost = {cost})", schedule)

    problem = ClassProblem1()
    schedule, cost = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=2,
        gamma=20,
        iterations=4,
        cost_function=sum_weighted_tardiness,
        verbose=True,
    )


    problem = ClassProblem2()
    schedule, cost = tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=2,
        gamma=100,
        iterations=3,
        cost_function=sum_weighted_tardiness,
        verbose=True,
    )


if __name__ == "__main__":
    main()
