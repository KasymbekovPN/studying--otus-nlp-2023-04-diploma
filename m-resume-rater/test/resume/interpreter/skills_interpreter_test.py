import unittest

from src.resume.interpreter.skills_interpreter import SkillsInterpreter
from src.resume import Resume, Part, Id
from src.result import Result


class TestCase(unittest.TestCase):
    ID = Id.url('https://10.0.0.1').value
    PART = Part('some.content')

    def test_raw_getting_if_resume_not_contain_cv_part(self):
        resume = Resume(self.ID)
        interpreter = SkillsInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.simple_fail('resume.skills.absence', id=self.ID)
        self.assertEqual(expected_result, result)

    def test_raw_getting(self):
        args = {Resume.SKILLS_KEYS[0]: self.PART}
        resume = Resume(self.ID, **args)
        interpreter = SkillsInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.ok(self.PART)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
