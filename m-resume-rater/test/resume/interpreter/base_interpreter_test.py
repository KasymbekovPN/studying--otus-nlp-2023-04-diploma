import unittest

from parameterized import parameterized
from src.resume.interpreter import BaseInterpreter
from src.utils import NGramsComputer, NWordsComputer
from src.result import Result
from src.resume import Resume, Id


class TestCase(unittest.TestCase):
    RESUME = Resume(Id.url('http://10.0.0.1').value)
    NGRAMS_COMPUTER = NGramsComputer()
    NWORDS_COMPUTER = NWordsComputer()
    BAD_KEY = BaseInterpreter.NGRAMS_COMPUTER_KEY + BaseInterpreter.NWORDS_COMPUTER_KEY + '!'

    class TestInterpreter(BaseInterpreter):
        def raw(self) -> Result:
            return Result.ok(None)

    class TestNGramsComputer(NGramsComputer):
        def __init__(self, result: Result) -> None:
            self._result = result

        def compute(self, inputs: tuple) -> Result:
            return self._result

    class TestNWordsComputer(NWordsComputer):
        def __init__(self, result: Result) -> None:
            self._result = result

        def compute(self, inputs: tuple) -> Result:
            return self._result

    @parameterized.expand([
        ({}, None),
        ({BAD_KEY: NGRAMS_COMPUTER}, None),
        ({BaseInterpreter.NGRAMS_COMPUTER_KEY: NGRAMS_COMPUTER}, NGRAMS_COMPUTER),
    ])
    def test_ngrams_computer_checking(self, args: dict, expected: NGramsComputer | None):
        result = BaseInterpreter.check_ngrams_computer(args)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ({}, None),
        ({BAD_KEY: NWORDS_COMPUTER}, None),
        ({BaseInterpreter.NWORDS_COMPUTER_KEY: NWORDS_COMPUTER}, NWORDS_COMPUTER),
    ])
    def test_nwords_computer_checking(self, args: dict, expected: NGramsComputer | None):
        result = BaseInterpreter.check_nwords_computer(args)
        self.assertEqual(expected, result)

    def test_raw_getting(self):
        interpreter = BaseInterpreter(self.RESUME)
        result = interpreter.raw()

        expected_result = Result.simple_fail(
            'interpreter.getting.raw.unsupported',
            class_name=BaseInterpreter.__name__
        )
        self.assertEqual(expected_result, result)

    def test_ngrams_getting_if_bas_raw_getting(self):
        interpreter = BaseInterpreter(self.RESUME)
        result = interpreter.ngrams()

        expected_result = Result.simple_fail(
            'interpreter.getting.raw.unsupported',
            class_name=BaseInterpreter.__name__
        )
        self.assertEqual(expected_result, result)

    def test_ngrams_getting_if_computer_none(self):
        interpreter = TestCase.TestInterpreter(self.RESUME)
        result = interpreter.ngrams()

        expected_result = Result.simple_fail(
            'interpreter.getting.ngrams.computer-absence',
            class_name=TestCase.TestInterpreter.__name__
        )
        self.assertEqual(expected_result, result)

    def test_ngrams_getting(self):
        expected_result = Result.ok('TestInterpreter')
        ngrams = TestCase.TestNGramsComputer(expected_result)
        args = {BaseInterpreter.NGRAMS_COMPUTER_KEY: ngrams}
        interpreter = TestCase.TestInterpreter(self.RESUME, **args)

        result = interpreter.ngrams()
        self.assertEqual(expected_result, result)

    def test_nwords_getting_if_bas_raw_getting(self):
        interpreter = BaseInterpreter(self.RESUME)
        result = interpreter.nwords()

        expected_result = Result.simple_fail(
            'interpreter.getting.raw.unsupported',
            class_name=BaseInterpreter.__name__
        )
        self.assertEqual(expected_result, result)

    def test_nwords_getting_if_computer_none(self):
        interpreter = TestCase.TestInterpreter(self.RESUME)
        result = interpreter.nwords()

        expected_result = Result.simple_fail(
            'interpreter.getting.nwords.computer-absence',
            class_name=TestCase.TestInterpreter.__name__
        )
        self.assertEqual(expected_result, result)

    def test_nwords_getting(self):
        expected_result = Result.ok('TestNWordsComputer')
        ngrams = TestCase.TestNWordsComputer(expected_result)
        args = {BaseInterpreter.NWORDS_COMPUTER_KEY: ngrams}
        interpreter = TestCase.TestInterpreter(self.RESUME, **args)

        result = interpreter.nwords()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
