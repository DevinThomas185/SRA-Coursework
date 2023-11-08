from Job import Job
from Problem import Problem


class ClassProblem1(Problem):
    def __init__(self):
        super().__init__()

        j1 = Job(1, 1, None, 16, 3)
        j2 = Job(2, 2, None, 11, 4)
        j3 = Job(3, 7, None, 4, 5)
        j4 = Job(4, 9, None, 8, 7)

        self._graph.add_node(j1)
        self._graph.add_node(j2)
        self._graph.add_node(j3)
        self._graph.add_node(j4)

        self._initial_candidate = [j4, j2, j1, j3]


class ClassProblem2(Problem):
    def __init__(self):
        super().__init__()

        j1 = Job(1, 4, None, 10, 14)
        j2 = Job(2, 2, None, 10, 12)
        j3 = Job(3, 1, None, 13, 1)
        j4 = Job(4, 12, None, 4, 12)

        self._graph.add_node(j1)
        self._graph.add_node(j2)
        self._graph.add_node(j3)
        self._graph.add_node(j4)

        self._initial_candidate = [j2, j1, j4, j3]