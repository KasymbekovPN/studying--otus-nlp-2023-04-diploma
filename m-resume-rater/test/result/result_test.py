import unittest

from parameterized import parameterized
from src.result.result import Result, Status


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


if __name__ == '__main__':
    unittest.main()
