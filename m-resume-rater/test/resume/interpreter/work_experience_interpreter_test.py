import unittest

from src.resume.interpreter.work_experience_interpreter import WorkExperienceInterpreter
from src.resume import Resume, Part, Id
from src.result import Result


class MyTestCase(unittest.TestCase):
    ID = Id.url('https://10.0.0.1').value
    PART = Part('some.content')

    def test_raw_getting_if_resume_not_contain_cv_part(self):
        resume = Resume(self.ID)
        interpreter = WorkExperienceInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.simple_fail('resume.work-experience.absence', id=self.ID)
        self.assertEqual(expected_result, result)

    def test_raw_getting(self):
        args = {Resume.WORK_EXPERIENCE_KEYS[0]: self.PART}
        resume = Resume(self.ID, **args)
        interpreter = WorkExperienceInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.ok(self.PART)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
