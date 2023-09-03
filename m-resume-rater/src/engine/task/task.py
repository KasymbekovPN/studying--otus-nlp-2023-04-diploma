from src.engine import TaskKind
from src.resume import Id as ResumeId


def generate_own_task_id(kind: TaskKind, prev_value: int):
    return prev_value + 1


class TaskId:
    def __init__(self,
                 resume: ResumeId,
                 own: int) -> None:
        self._resume = resume
        self._own = own

    def __repr__(self):
        return f'TaskId {{ resume: {self.resume.value}, own: {self.own} }}'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.resume == other.resume and self.own == other.own

    @property
    def resume(self):
        return self._resume

    @property
    def own(self):
        return self._own

