import argparse

# Utilities
from utilities.utilities import format_number, print_schedule_to_csv, print_schedule

# Functions
from schedulers.tabu_search import tabu_search
from schedulers.variable_neighbourhood_search import variable_neighbourhood_search
from utilities.cost_functions import (
    sum_tardiness,
    sum_weighted_tardiness,
    total_tardy_jobs,
    weighted_total_tardy_jobs,
    maximum_tardiness,
    maximum_completion_time,
    sum_completion_time,
    sum_lateness,
    sum_weighted_lateness,
    maximum_lateness,
)


# Problems
from classes.Problem import Problem
from classes.CourseworkProblem import CourseworkProblem
from classes.ClassProblems import ClassProblem1, ClassProblem2, MatrixProblem


if __name__ == "__main__":
    # Argparse
    cost_function_mappings = {
        "sum_tardiness": sum_tardiness,
        "sum_weighted_tardiness": sum_weighted_tardiness,
        "total_tardy_jobs": total_tardy_jobs,
        "weighted_total_tardy_jobs": weighted_total_tardy_jobs,
        "maximum_tardiness": maximum_tardiness,
        "maximum_completion_time": maximum_completion_time,
        "sum_completion_time": sum_completion_time,
        "sum_lateness": sum_lateness,
        "sum_weighted_lateness": sum_weighted_lateness,
        "maximum_lateness": maximum_lateness,
    }
    default_problem_mappings = {
        "ClassProblem1": ClassProblem1,
        "ClassProblem2": ClassProblem2,
        "MatrixProblem": MatrixProblem,
        "CourseworkProblem": CourseworkProblem,
    }

    parser = argparse.ArgumentParser(description="Optimal Schedule Discovery")
    parser.add_argument(
        "scheduler",
        choices=["tabu_search", "vn_search"],
        help="Select a scheduler",
    )
    parser.add_argument(
        "cost_function",
        choices=cost_function_mappings.keys(),
        help="Cost function to evaluate candidate schedules",
    )
    parser.add_argument(
        "--tabu_list_size",
        type=int,
        default=20,
        help="Tabu list size for Tabu Search",
    )
    parser.add_argument(
        "--strict_tabu_tenure",
        action="store_true",
        help="Strict tabu tenure for Tabu Search",
    )
    parser.add_argument(
        "--gamma",
        type=int,
        default=10,
        help="Gamma value",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=10_000_000,
        help="Number of iterations",
    )
    parser.add_argument(
        "--I",
        type=int,
        default=10,
        help="Maximum I for neighbourhood generation in Variable Neighbourhood Search",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose mode",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default=None,
        help="Save schedule to output file",
    )
    parser.add_argument(
        "--graph_schedule",
        action="store_true",
        help="Graph optimal schedule",
    )
    parser.add_argument(
        "--execution_output_file",
        type=str,
        default=None,
        help="Save execution (AKA verbose output) to output file",
    )
    parser.add_argument(
        "--apply_local_optimisation",
        action="store_true",
        help="Apply local optimisation in VNS",
    )

    exclusive_group = parser.add_mutually_exclusive_group(required=True)

    exclusive_group.add_argument(
        "--problem",
        choices=default_problem_mappings.keys(),
        default="coursework_problem",
        help="Problem to solve",
    )
    exclusive_group.add_argument(
        "--problem_from_file",
        type=str,
        default=None,
        help="Provide problem definition from file",
    )

    args = parser.parse_args()

    problem_title = ""
    if args.problem_from_file:
        problem_title = args.problem_from_file
        problem = Problem()
        problem.load_from_file(args.problem_from_file)
        problem.__post_init__()
    else:
        problem_title = args.problem
        problem = default_problem_mappings[args.problem]()

    scheduler_title = ""
    schedule = []
    cost = 0

    if args.scheduler == "tabu_search":
        scheduler_title = "Tabu Search"
        schedule, cost, _ = tabu_search(
            problem=problem,
            tabu_list_size=args.tabu_list_size,
            gamma=args.gamma,
            iterations=args.iterations,
            cost_function=cost_function_mappings[args.cost_function],
            strict_tabu_tenure=args.strict_tabu_tenure,
            verbose=args.verbose,
            print_file=args.execution_output_file,
        )

    elif args.scheduler == "vn_search":
        scheduler_title = "Variable Neighbourhood Search"
        schedule, cost, _ = variable_neighbourhood_search(
            problem=problem,
            cost_function=cost_function_mappings[args.cost_function],
            iterations=args.iterations,
            I=args.I,
            verbose=args.verbose,
            print_file=args.execution_output_file,
            apply_tabu_search=args.apply_local_optimisation,
        )

    print()
    print(f"Schedule: {schedule}")
    print(f"Cost: {cost}")

    if args.output_file:
        print_schedule_to_csv(schedule, args.output_file)

    if args.graph_schedule:
        print_schedule(
            f"Optimal schedule for {problem_title}, after K={format_number(args.iterations)} of {scheduler_title}, with L={args.tabu_list_size} and γ={args.gamma}, has cost {cost}",
            schedule,
        )
