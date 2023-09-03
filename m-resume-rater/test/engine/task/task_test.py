import unittest

from parameterized import parameterized
from src.resume import Id as ResumeId
from src.engine.task.task_id import TaskId
from src.engine.task.task import Task
from src.resume import Part


class TestCase(unittest.TestCase):
    _TASK_ID = TaskId(ResumeId.url('https://10.0.0.1').value, 1)
    _PART = Part('hello', 'world')

    def test_task_id_getting(self):
        task = Task(self._TASK_ID, self._PART)
        self.assertEqual(self._TASK_ID, task.task_id)

    def test_task_part_getting(self):
        task = Task(self._TASK_ID, self._PART)
        self.assertEqual(self._PART, task.part)

    @parameterized.expand([
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                None,
                False
        ),
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                123,
                False
        ),
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                Task(TaskId(ResumeId.url('https://10.0.0.2').value, 1), Part('1')),
                False
        ),
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 2), Part('1')),
                False
        ),
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('2')),
                False
        ),
        (
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                Task(TaskId(ResumeId.url('https://10.0.0.1').value, 1), Part('1')),
                True
        ),
    ])
    def test_task_eq(self, first: Task, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_test_repr(self):
        task_id = TaskId(ResumeId.url('https://10.0.0.1').value, 1)
        part = Part('hello')
        task = Task(task_id, part)
        expected = f'Task {{ id: {task_id}, {part}'

        self.assertEqual(expected, task.__repr__())


if __name__ == '__main__':
    unittest.main()
