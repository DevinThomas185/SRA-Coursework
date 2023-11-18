from Job import Job, JobType
from DirectedAcyclicGraph import DirectedAcyclicGraph
import json


class Problem:
    __slots__ = [
        "_graph",
        "_initial_candidate",
        "_problem_name",
    ]

    def __init__(self):
        self._graph = DirectedAcyclicGraph()
        self._initial_candidate = []

    def __post_init__(self):
        self._graph.compute_transitive_closure()

    def get_problem_name(self):
        return self._problem_name

    def get_graph(self) -> DirectedAcyclicGraph:
        return self._graph

    def get_schedule_size(self) -> int:
        return self._graph.get_job_size()

    def get_initial_candidate(self) -> list:
        return self._initial_candidate

    def set_initial_candidate(self, initial_candidate: list):
        self._initial_candidate = initial_candidate

    def _get_job_type(self, name: str):
        return JobType[name.split("_")[0].upper()]

    def _find_initial_candidate(self) -> list:
        levels = []
        last_level = []
        current_level = []

        incidence_matrix = self._graph.get_incidence_matrix()

        # Find row in incidence matrix with all zeros to set as bottom level
        for i in range(self._graph.get_job_size()):
            if not any(incidence_matrix[i]):
                current_level.append(self._graph.get_jobs()[i + 1])

        levels.append(current_level)
        last_level = current_level
        current_level = []

        # Find the rest of the levels
        while last_level:
            for job in last_level:
                for i in range(self._graph.get_job_size()):
                    if incidence_matrix[i, job.get_id() - 1] == 1:
                        current_level.append(self._graph.get_jobs()[i + 1])
            levels.append(current_level)
            last_level = current_level
            current_level = []

        for level in levels[::-1]:
            self._initial_candidate.extend(level)

        # Remove duplicates past first occurrence of each job since we need to take the highest level
        self._initial_candidate = list(dict.fromkeys(self._initial_candidate))

    def load_from_file(self, input_file: str):
        with open(input_file, "r") as f:
            data = json.load(f)["workflow_0"]

            jobs = {}

            for i, node in enumerate(data["due_dates"]):
                j = Job(
                    id=i + 1,
                    due_date=data["due_dates"][node],
                    type=self._get_job_type(node),
                )
                jobs[node] = j
                self._graph.add_node(j)

            for edge in data["edge_set"]:
                self._graph.add_precendence(jobs[edge[0]], jobs[edge[1]])

            self._find_initial_candidate()
