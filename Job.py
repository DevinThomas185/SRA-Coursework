from enum import Enum


class JobType(Enum):
    VII = 0
    EMBOSS = 1
    MUSE = 2
    NIGHT = 3
    BLUR = 4
    WAVE = 5
    ONNX = 6


PROCESSING_TIMES = {
    JobType.VII: 14,
    JobType.EMBOSS: 2,
    JobType.MUSE: 10,
    JobType.NIGHT: 18,
    JobType.BLUR: 5,
    JobType.WAVE: 6,
    JobType.ONNX: 3,
}


class Job:
    __slots__ = [
        "_id",
        "_type",
        "_due_date",
        "_processing_time",
        "_weight",
        "_colour",
    ]

    def __init__(
        self,
        id: int,
        due_date: int,
        type: JobType = None,
        processing_time: int = 0,
        weight: int = 1,
        colour: str = None,
    ):
        self._id = id
        self._type = type
        self._due_date = due_date
        self._processing_time = (
            processing_time if type is None else PROCESSING_TIMES[type]
        )
        self._weight = weight
        self._colour = colour

    def __repr__(self):
        return str(self._id)

    def get_id(self) -> int:
        return self._id

    def get_due_date(self) -> int:
        return self._due_date

    def get_processing_time(self) -> int:
        return self._processing_time

    def get_weight(self) -> int:
        return self._weight

    def get_colour(self) -> str:
        return self._colour
