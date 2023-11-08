from Job import Job, JobType
from Problem import Problem

class CWProblem(Problem):

    def __init__(self):
        super().__init__()

        j1 = Job(1, 172, JobType.ONNX)
        j2 = Job(2, 82, JobType.MUSE)
        j3 = Job(3, 18, JobType.EMBOSS)
        j4 = Job(4, 61, JobType.EMBOSS)
        j5 = Job(5, 93, JobType.BLUR)
        j6 = Job(6, 71, JobType.EMBOSS)
        j7 = Job(7, 217, JobType.VII)
        j8 = Job(8, 295, JobType.BLUR)
        j9 = Job(9, 290, JobType.WAVE)
        j10 = Job(10, 287, JobType.BLUR)
        j11 = Job(11, 253, JobType.BLUR)
        j12 = Job(12, 307, JobType.EMBOSS)
        j13 = Job(13, 279, JobType.ONNX)
        j14 = Job(14, 73, JobType.ONNX)
        j15 = Job(15, 355, JobType.BLUR)
        j16 = Job(16, 34, JobType.WAVE)
        j17 = Job(17, 233, JobType.WAVE)
        j18 = Job(18, 77, JobType.WAVE)
        j19 = Job(19, 88, JobType.EMBOSS)
        j20 = Job(20, 122, JobType.ONNX)
        j21 = Job(21, 71, JobType.EMBOSS)
        j22 = Job(22, 181, JobType.ONNX)
        j23 = Job(23, 340, JobType.VII)
        j24 = Job(24, 141, JobType.BLUR)
        j25 = Job(25, 209, JobType.NIGHT)
        j26 = Job(26, 217, JobType.MUSE)
        j27 = Job(27, 256, JobType.EMBOSS)
        j28 = Job(28, 144, JobType.ONNX)
        j29 = Job(29, 307, JobType.WAVE)
        j30 = Job(30, 329, JobType.EMBOSS)
        j31 = Job(31, 269, JobType.EMBOSS)

        self._graph.add_node(j1)
        self._graph.add_node(j2)
        self._graph.add_node(j3)
        self._graph.add_node(j4)
        self._graph.add_node(j5)
        self._graph.add_node(j6)
        self._graph.add_node(j7)
        self._graph.add_node(j8)
        self._graph.add_node(j9)
        self._graph.add_node(j10)
        self._graph.add_node(j11)
        self._graph.add_node(j12)
        self._graph.add_node(j13)
        self._graph.add_node(j14)
        self._graph.add_node(j15)
        self._graph.add_node(j16)
        self._graph.add_node(j17)
        self._graph.add_node(j18)
        self._graph.add_node(j19)
        self._graph.add_node(j20)
        self._graph.add_node(j21)
        self._graph.add_node(j22)
        self._graph.add_node(j23)
        self._graph.add_node(j24)
        self._graph.add_node(j25)
        self._graph.add_node(j26)
        self._graph.add_node(j27)
        self._graph.add_node(j28)
        self._graph.add_node(j29)
        self._graph.add_node(j30)
        self._graph.add_node(j31)

        # Add the precedences from below
        self._graph.add_precendence(j1, j31)
        self._graph.add_precendence(j2, j1)
        self._graph.add_precendence(j3, j8)
        self._graph.add_precendence(j4, j3)
        self._graph.add_precendence(j5, j2)
        self._graph.add_precendence(j6, j16)
        self._graph.add_precendence(j7, j6)
        self._graph.add_precendence(j8, j7)
        self._graph.add_precendence(j9, j8)
        self._graph.add_precendence(j10, j9)
        self._graph.add_precendence(j11, j1)
        self._graph.add_precendence(j12, j5)
        self._graph.add_precendence(j13, j12)
        self._graph.add_precendence(j14, j13)
        self._graph.add_precendence(j17, j15)
        self._graph.add_precendence(j15, j11)
        self._graph.add_precendence(j16, j5)
        self._graph.add_precendence(j17, j16)
        self._graph.add_precendence(j18, j17)
        self._graph.add_precendence(j19, j18)
        self._graph.add_precendence(j20, j19)
        self._graph.add_precendence(j21, j18)
        self._graph.add_precendence(j22, j21)
        self._graph.add_precendence(j23, j22)
        self._graph.add_precendence(j24, j5)
        self._graph.add_precendence(j25, j24)
        self._graph.add_precendence(j26, j25)
        self._graph.add_precendence(j27, j26)
        self._graph.add_precendence(j28, j26)
        self._graph.add_precendence(j29, j28)
        self._graph.add_precendence(j29, j27)
        self._graph.add_precendence(j30, j4)
        self._graph.add_precendence(j30, j10)
        self._graph.add_precendence(j30, j14)
        self._graph.add_precendence(j30, j20)
        self._graph.add_precendence(j30, j23)
        self._graph.add_precendence(j30, j27)
        self._graph.add_precendence(j30, j29)

        self._initial_candidate = [
            j30,
            j29,
            j23,
            j10,
            j9,
            j14,
            j13,
            j12,
            j4,
            j20,
            j22,
            j3,
            j27,
            j28,
            j8,
            j7,
            j19,
            j21,
            j26,
            j18,
            j25,
            j17,
            j15,
            j6,
            j24,
            j16,
            j5,
            j11,
            j2,
            j1,
            j31,
        ]