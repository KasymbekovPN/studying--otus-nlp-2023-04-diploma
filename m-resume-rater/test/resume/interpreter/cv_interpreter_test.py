import unittest

from src.resume.interpreter.cv_interpreter import CVInterpreter
from src.resume import Resume, Part, Id
from src.result import Result


class TestCase(unittest.TestCase):
    ID = Id.url('https://10.0.0.1').value
    PART = Part('some.content')

    def test_raw_getting_if_resume_not_contain_cv_part(self):
        resume = Resume(self.ID)
        interpreter = CVInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.simple_fail('resume.cv.absence', id=self.ID)
        self.assertEqual(expected_result, result)

    def test_raw_getting(self):
        args = {Resume.CV_KEYS[0]: self.PART}
        resume = Resume(self.ID, **args)
        interpreter = CVInterpreter(resume)
        result = interpreter.raw()

        expected_result = Result.ok(self.PART)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
