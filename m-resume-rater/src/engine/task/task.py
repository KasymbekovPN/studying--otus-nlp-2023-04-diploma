from src.engine import TaskId
from src.resume import Part as ResumePart


# todo del
class Task:
    def __init__(self, task_id: TaskId, part: ResumePart):
        self._task_id = task_id
        self._part = part

    def __repr__(self):
        return f'Task {{ id: {self.task_id}, {self.part}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.task_id == other.task_id and self.part == other.part

    @property
    def task_id(self):
        return self._task_id

    @property
    def part(self):
        return self._part
