import unittest
import random

from parameterized import parameterized
from src.resume import Id as ResumeId
from src.engine import TaskKind
from src.engine.task.task import generate_own_task_id, TaskId


# todo impl
class TestCase(unittest.TestCase):
    _RESUME_ID = ResumeId.url('https://10.0.0.1').value

    @parameterized.expand([
        (TaskKind.CV, 1, 2),
        (TaskKind.EDUCATION, 2, 3),
        (TaskKind.REFRESHER_COURSES, 3, 4),
        (TaskKind.SHUTDOWN, 5, 6),
        (TaskKind.SKILLS, 6, 7),
        (TaskKind.SPECIALIZATION, 7, 8),
        (TaskKind.WORK_EXPERIENCE, 9, 10),
    ])
    def test_default_own_task_id_generation(self, kind: TaskKind, prev: int, expected: int):
        own_id = generate_own_task_id(kind, prev)
        self.assertEqual(expected, own_id)

    def test_task_id_resume_part_getting(self):
        task_id = TaskId(self._RESUME_ID, 0)
        self.assertEqual(self._RESUME_ID, task_id.resume)

    def test_task_id_own_part_getting(self):
        expected_own_id = random.randrange(100)
        task_id = TaskId(self._RESUME_ID, expected_own_id)
        self.assertEqual(expected_own_id, task_id.own)

    @parameterized.expand([
        (TaskId(ResumeId.url('https://10.0.0.1').value, 1), None, False),
        (TaskId(ResumeId.url('https://10.0.0.1').value, 1), 123, False),
        (
                TaskId(ResumeId.url('https://10.0.0.1').value, 1),
                TaskId(ResumeId.url('https://10.0.0.1').value, 2),
                False
        ),
        (
                TaskId(ResumeId.url('https://10.0.0.2').value, 1),
                TaskId(ResumeId.url('https://10.0.0.1').value, 2),
                False
        ),
        (
                TaskId(ResumeId.url('https://10.0.0.1').value, 1),
                TaskId(ResumeId.url('https://10.0.0.2').value, 2),
                False
        ),
        (
                TaskId(ResumeId.url('https://10.0.0.1').value, 1),
                TaskId(ResumeId.url('https://10.0.0.1').value, 1),
                True
        ),
    ])
    def test_task_id_eq(self, first: TaskId, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_test_id_repr(self):
        url = 'https://10.0.0.1'
        own_id = 1
        resume_id = ResumeId.url(url).value
        expected = f'TaskId {{ resume: {url}, own: {own_id} }}'

        task_id = TaskId(resume_id, own_id)
        self.assertEqual(expected, task_id.__repr__())


if __name__ == '__main__':
    unittest.main()
