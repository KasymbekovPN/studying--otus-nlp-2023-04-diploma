import unittest

from parameterized import parameterized
from src.resume import Id, Part, Resume, Entity


class TestCase(unittest.TestCase):

    ID = Id.url('http://10.0.0.1').value

    @parameterized.expand([
        (Id.url('http://10.0.0.2').value, Id.url('http://10.0.0.2').value),
        (Id.url('http://10.0.0.3').value, Id.url('http://10.0.0.3').value),
        (Id.url('http://10.0.0.4').value, Id.url('http://10.0.0.4').value)
    ])
    def test_resume_id_getting(self, init_id: Id, expected_id: Id):
        resume = Resume(init_id)
        self.assertEqual(expected_id, resume.resume_id)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_getting(self, init_part: Part, expected_part: Part):
        for entity in Entity:
            args = {entity.value[1]: init_part}
            resume = Resume(TestCase.ID, **args)
            self.assertEqual(expected_part, resume.get(entity))

    @parameterized.expand([
        (Part('p0'), ),
        (Part('p0', 'p1'), ),
    ])
    def test_setting(self, expected_part: Part):
        for entity in Entity:
            resume = Resume(TestCase.ID)
            self.assertEqual(None, resume.get(entity))
            resume.set(entity, expected_part)
            self.assertEqual(expected_part, resume.get(entity))


if __name__ == '__main__':
    unittest.main()
