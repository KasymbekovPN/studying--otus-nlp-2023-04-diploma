import unittest

from parameterized import parameterized
from src.resume.parts.part import Part


class TestCase(unittest.TestCase):
    @parameterized.expand([
        ([123, '123', None, '456'], ('123', '456')),
        ([123, None], ()),
        (['123', '456'], ('123', '456'))
    ])
    def test_init_and_raw_getting(self, init_data: list, expected_value: tuple):
        part = Part(*init_data)
        self.assertTupleEqual(expected_value, part.value)

    @parameterized.expand([
        (['hello', 'world'], "Part ('hello', 'world')"),
        (['world', 'hello'], "Part ('world', 'hello')")
    ])
    def test_repr(self, init_data: tuple, expected: str):
        parts = Part(*init_data)
        self.assertEqual(expected, parts.__repr__())

    @parameterized.expand([
        (Part('hello', 'world'), Part('hello', 'world'), True),
        (Part('hello', 'world'), Part('world', 'hello'), False),
        (Part('hello', 'world'), ('world', 'hello'), False)
    ])
    def test_eq(self, first: Part, second: Part, expected: bool):
        self.assertEqual(expected, first == second)


if __name__ == '__main__':
    unittest.main()
