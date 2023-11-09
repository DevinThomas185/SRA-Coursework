import numpy as np
from Job import Job
from graphviz import Digraph


class DirectedAcyclicGraph:
    __slots__ = [
        "_jobs",
        "_incidence_matrix",
        "_transitive_closure"
    ]

    def __init__(self):
        self._jobs = []

    def add_node(self, job: Job) -> None:
        self._jobs.append(job)

        # Reset the matrix
        self._incidence_matrix = np.zeros((len(self._jobs), len(self._jobs)))

    def add_precendence(self, job: Job, precendence: Job) -> None:
        self._incidence_matrix[job.get_id() - 1, precendence.get_id() - 1] = 1

    def compute_transitive_closure(self) -> None:
        # Compute the transitive closure of the incidence matrix. I.e if matrix[i, j] == 1, and matrix[j, k] == 1, then matrix[i, k] == 1
        self._transitive_closure = self._incidence_matrix.copy()
        for i in range(len(self._jobs)):
            for j in range(len(self._jobs)):
                if self._transitive_closure[j, i] == 1:
                    for k in range(len(self._jobs)):
                        if self._transitive_closure[i, k] == 1:
                            self._transitive_closure[j, k] = 1

    def get_transitive_closure(self) -> np.ndarray:
        return self._transitive_closure

    def print_graph(self) -> None:
        g = Digraph("G", filename="dag.gv")

        g.attr(rankdir="TB", size="8,5")

        g.attr("node", shape="circle")

        # Add node for each job
        for job in self._jobs:
            g.node(str(job.get_id()))

        # Add edges
        for i in range(len(self._jobs)):
            for j in range(len(self._jobs)):
                if self._incidence_matrix[i, j] == 1:
                    g.edge(str(i + 1), str(j + 1))

        g.view()
