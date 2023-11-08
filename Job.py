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
    JobType.EMBOSS: 5,
    JobType.MUSE: 18,
    JobType.NIGHT: 3,
    JobType.BLUR: 2,
    JobType.WAVE: 10,
    JobType.ONNX: 6,
}


class Job:
    __slots__ = [
        "_id",
        "_type",
        "_due_date",
        "_processing_time",
        "_weight",
    ]

    def __init__(
        self, id: int, due_date: int, type: JobType = None, processing_time: int = 0, weight: int = 1
    ):
        self._id = id
        self._type = type
        self._due_date = due_date
        self._processing_time = (
            processing_time if type is None else PROCESSING_TIMES[type]
        )
        self._weight = weight

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
