import unittest

from parameterized import parameterized
from src.result import Result, Status


class TestCase(unittest.TestCase):

    @parameterized.expand([
        ('template.0', {}, {}),
        ('template.1', {'a': 0, 'b': '123'}, {'a': 0, 'b': '123'}),
        ('template.1', None, {})
    ])
    def test_status_creation(self, template: str, args: dict | None, expected_args: dict):
        status = Status(template, **args) if args is not None else Status(template)
        self.assertEqual(template, status.template)
        self.assertEqual(expected_args, status.args)

    @parameterized.expand([
        (True,),
        (False,)
    ])
    def test_success_getter(self, expected_success: bool):
        r = Result(expected_success, None, [])
        self.assertEqual(r.success, expected_success)

    @parameterized.expand([
        (1,),
        ("1",),
        ({"1": 1},),
        None
    ])
    def test_value_getter(self, expected_value):
        r = Result(True, expected_value, [])
        self.assertEqual(r.value, expected_value)

    @parameterized.expand([
        ([Status("template.0")], [Status("template.0")]),
        (
                [Status("template.0"), Status("template.0", x=123)],
                [Status("template.0"), Status("template.0", x=123)]
        ),
        (None, [])
    ])
    def test_statuses_getter(self, statuses, expected_statuses):
        r = Result(False, None, statuses)
        self.assertEqual(r.statuses, expected_statuses)

    @parameterized.expand([
        (123,),
        ("123",)
    ])
    def test_ok_result_creation(self, value):
        r = Result.ok(value)
        self.assertEqual(r, Result(True, value, []))

    @parameterized.expand([
        (Status("template.0"),),
        (Status("template.1", x=123),)
    ])
    def test_fail_result_creation(self, status: Status):
        r = Result.fail(status)
        self.assertEqual(r, Result(False, None, [status]))

    @parameterized.expand([
        ("template.0",),
        ("template.1",)
    ])
    def test_simple_fail_result_creation(self, template: str):
        r = Result.simple_fail(template)
        self.assertEqual(r, Result(False, None, [Status(template)]))

    @parameterized.expand([
        (False, None, [Status("template.0")]),
        (True, 123, [])
    ])
    def test_full_result_creation(self, expected_success: bool, expected_value, expected_statuses: list):
        r = Result.full(expected_success, expected_value, expected_statuses)
        self.assertEqual(r, Result(expected_success, expected_value, expected_statuses))


if __name__ == '__main__':
    unittest.main()
