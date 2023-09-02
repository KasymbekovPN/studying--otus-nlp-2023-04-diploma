import unittest

from parameterized import parameterized
from src.resume import Id, Part, Resume


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
    def test_short_about_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.SHORT_ABOUT_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.short_about)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_specialization_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.SPECIALIZATION_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.specialization)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_cv_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.CV_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.cv)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_education_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.EDUCATION_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.education)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_refresher_courses_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.REFRESHER_COURSES_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.refresher_courses)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_work_experience_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.WORK_EXPERIENCE_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.work_experience)

    @parameterized.expand([
        (Part('p0'), Part('p0')),
        (Part('p0', 'p1'), Part('p0', 'p1')),
    ])
    def test_skills_getting(self, init_part: Part, expected_part: Part):
        args = {Resume.SKILLS_KEYS[0]: init_part}
        resume = Resume(TestCase.ID, **args)
        self.assertEqual(expected_part, resume.skills)


if __name__ == '__main__':
    unittest.main()
