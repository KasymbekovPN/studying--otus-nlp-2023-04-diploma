import unittest

from parameterized import parameterized
from src.resume import Id as ResumeId
from src.rate import Rate
from src.conversation.conductor.response import Response


class TestCase(unittest.TestCase):
    _IDX = 123
    _RESUME_ID = ResumeId.url('https://10.0.0.1').value
    _RATE = Rate(0)

    def test_response_idx_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE)
        self.assertEqual(self._IDX, response.idx)

    def test_response_resume_id_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE)
        self.assertEqual(self._RESUME_ID, response.resume_id)

    def test_response_rate_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE)
        self.assertEqual(self._RATE, response.rate)

    @parameterized.expand([
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                None,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                123,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                Response(2, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                Response(1, ResumeId.url('https://10.0.0.2').value, Rate(1)),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(2)),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1)),
                True
        ),
    ])
    def test_request_eq(self, first: Response, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_response_repr(self):
        request = Response(self._IDX, self._RESUME_ID, self._RATE)
        expected = f'Request {{id: {self._IDX}}}'

        self.assertEqual(expected, request.__repr__())


if __name__ == '__main__':
    unittest.main()
