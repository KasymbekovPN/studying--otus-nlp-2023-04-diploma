import unittest

from parameterized import parameterized
from src.resume import Id as ResumeId, Part
from src.conversation.engine.request import Request


class TestCase(unittest.TestCase):
    _IDX = 123
    _RESUME_ID = ResumeId.url('https://10.0.0.1').value
    _PART = Part('hello', 'world')

    def test_request_idx_getting(self):
        request = Request(self._IDX, self._RESUME_ID, self._PART)
        self.assertEqual(self._IDX, request.idx)

    def test_request_resume_id_getting(self):
        request = Request(self._IDX, self._RESUME_ID, self._PART)
        self.assertEqual(self._RESUME_ID, request.resume_id)

    def test_request_part_getting(self):
        request = Request(self._IDX, self._RESUME_ID, self._PART)
        self.assertEqual(self._PART, request.part)

    @parameterized.expand([
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                None,
                False
        ),
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                123,
                False
        ),
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                Request(2, ResumeId.url('https://10.0.0.1').value, Part('1')),
                False
        ),
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                Request(1, ResumeId.url('https://10.0.0.2').value, Part('1')),
                False
        ),
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('2')),
                False
        ),
        (
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                Request(1, ResumeId.url('https://10.0.0.1').value, Part('1')),
                True
        )
    ])
    def test_request_eq(self, first: Request, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_request_repr(self):
        request = Request(self._IDX, self._RESUME_ID, self._PART)
        expected = f'Request {{id: {self._IDX}, resume_id: {self._RESUME_ID} }}'

        self.assertEqual(expected, request.__repr__())


if __name__ == '__main__':
    unittest.main()
