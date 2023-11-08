from Job import Job, JobType
from DirectedAcyclicGraph import DirectedAcyclicGraph

class Problem:
    __slots__ = [
        "_graph",
        "_initial_candidate",
    ]

    def __init__(self):
        self._graph = DirectedAcyclicGraph()
        self._initial_candidate = []

    def get_graph(self) -> DirectedAcyclicGraph:
        return self._graph

    def get_initial_candidate(self) -> list:
        return self._initial_candidate
