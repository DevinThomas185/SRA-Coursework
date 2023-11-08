from Job import Job, JobType
from DirectedAcyclicGraph import DirectedAcyclicGraph
from tabu_search import tabu_search
from cost_functions import sum_tardiness, sum_weighted_tardiness

from CourseworkProblem import CourseworkProblem
from ClassProblem import ClassProblem


def main():
    problem = CourseworkProblem()
    tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=20,
        gamma=10,
        iterations=100000,
        cost_function=sum_tardiness,
        verbose=True,
    )

    problem = ClassProblem()
    tabu_search(
        graph=problem.get_graph(),
        initial_candidate=problem.get_initial_candidate(),
        tabu_list_size=2,
        gamma=20,
        iterations=5,
        cost_function=sum_weighted_tardiness,
        verbose=True,
    )


if __name__ == "__main__":
    main()
