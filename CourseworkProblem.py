from Job import Job, JobType
from Problem import Problem
from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np


class CourseworkProblem(Problem):
    def __init__(self):
        super().__init__()

        # Define the number of colors you need

        color_map = plt.get_cmap('nipy_spectral')
        colours = [colors.to_hex(color_map(value)) for value in np.linspace(0, 1, 31)]

        j1 = Job(1, due_date=172, type=JobType.ONNX, colour=colours[0])
        j2 = Job(2, due_date=82, type=JobType.MUSE, colour=colours[1])
        j3 = Job(3, due_date=18, type=JobType.EMBOSS, colour=colours[2])
        j4 = Job(4, due_date=61, type=JobType.EMBOSS, colour=colours[3])
        j5 = Job(5, due_date=93, type=JobType.BLUR, colour=colours[4])
        j6 = Job(6, due_date=71, type=JobType.EMBOSS, colour=colours[5])
        j7 = Job(7, due_date=217, type=JobType.VII, colour=colours[6])
        j8 = Job(8, due_date=295, type=JobType.BLUR, colour=colours[7])
        j9 = Job(9, due_date=290, type=JobType.WAVE, colour=colours[8])
        j10 = Job(10, due_date=287, type=JobType.BLUR, colour=colours[9])
        j11 = Job(11, due_date=253, type=JobType.BLUR, colour=colours[10])
        j12 = Job(12, due_date=307, type=JobType.EMBOSS, colour=colours[11])
        j13 = Job(13, due_date=279, type=JobType.ONNX, colour=colours[12])
        j14 = Job(14, due_date=73, type=JobType.ONNX, colour=colours[13])
        j15 = Job(15, due_date=355, type=JobType.BLUR, colour=colours[14])
        j16 = Job(16, due_date=34, type=JobType.WAVE, colour=colours[15])
        j17 = Job(17, due_date=233, type=JobType.WAVE, colour=colours[16])
        j18 = Job(18, due_date=77, type=JobType.WAVE, colour=colours[17])
        j19 = Job(19, due_date=88, type=JobType.EMBOSS, colour=colours[18])
        j20 = Job(20, due_date=122, type=JobType.ONNX, colour=colours[19])
        j21 = Job(21, due_date=71, type=JobType.EMBOSS, colour=colours[20])
        j22 = Job(22, due_date=181, type=JobType.ONNX, colour=colours[21])
        j23 = Job(23, due_date=340, type=JobType.VII, colour=colours[22])
        j24 = Job(24, due_date=141, type=JobType.BLUR, colour=colours[23])
        j25 = Job(25, due_date=209, type=JobType.NIGHT, colour=colours[24])
        j26 = Job(26, due_date=217, type=JobType.MUSE, colour=colours[25])
        j27 = Job(27, due_date=256, type=JobType.EMBOSS, colour=colours[26])
        j28 = Job(28, due_date=144, type=JobType.ONNX, colour=colours[27])
        j29 = Job(29, due_date=307, type=JobType.WAVE, colour=colours[28])
        j30 = Job(30, due_date=329, type=JobType.EMBOSS, colour=colours[29])
        j31 = Job(31, due_date=269, type=JobType.EMBOSS, colour=colours[30])

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
