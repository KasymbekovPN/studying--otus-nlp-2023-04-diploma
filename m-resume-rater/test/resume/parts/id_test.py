import unittest

from parameterized import parameterized

from src.result import Result, Status
from src.resume.parts.id import Id, IdKind


class TestCase(unittest.TestCase):

    @parameterized.expand([
        (IdKind.URL,)
    ])
    def test_kind_getter(self, expected_kind: IdKind):
        rid = Id(expected_kind, None)
        self.assertEqual(rid.kind, expected_kind)

    @parameterized.expand([
        (123,),
        ("123",),
        (None,)
    ])
    def test_value_getter(self, expected_value):
        rid = Id(IdKind.URL, expected_value)
        self.assertEqual(rid.value, expected_value)

    @parameterized.expand([
        ('http://example.com/">user@example.com', )
    ])
    def test_fail_url_result_id_creation(self, url: str):
        result = Id.url(url)
        self.assertEqual(result, Result.fail(Status('resume.id.creation.bad-url', url=url)))

    @parameterized.expand([
        ('http://duck.com', ),
        ('ftp://foobar.dk',),
        ('http://10.0.0.1',)
    ])
    def test_success_url_result_id_creation(self, url: str):
        result = Id.url(url)
        self.assertEqual(result, Result.ok(Id(IdKind.URL, url)))


if __name__ == '__main__':
    unittest.main()
