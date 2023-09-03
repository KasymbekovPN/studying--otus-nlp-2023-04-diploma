import unittest

from parameterized import parameterized
from src.resume import Resume, Id as ResumeId
from src.conversation.conductor.request import Request


class TestCase(unittest.TestCase):
    _RESUME = Resume(ResumeId.url('https://10.0.0.1').value)
    _IDX = 123

    def test_request_idx_getting(self):
        request = Request(self._IDX, self._RESUME)
        self.assertEqual(self._IDX, request.idx)

    def test_request_resume_getting(self):
        request = Request(self._IDX, self._RESUME)
        self.assertEqual(self._RESUME, request.resume)

    @parameterized.expand([
        (
                Resume(ResumeId.url('https://10.0.0.1').value),
                None,
                False
        ),
        (
                Resume(ResumeId.url('https://10.0.0.1').value),
                123,
                False
        ),
        (
                Resume(ResumeId.url('https://10.0.0.1').value),
                Resume(ResumeId.url('https://10.0.0.2').value),
                False
        ),
        (
                Resume(ResumeId.url('https://10.0.0.1').value),
                Resume(ResumeId.url('https://10.0.0.1').value),
                True
        ),
    ])
    def test_request_eq(self, first: Request, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_request_repr(self):
        request = Request(self._IDX, self._RESUME)
        expected = f'Request {{id: {self._IDX}}}'

        self.assertEqual(expected, request.__repr__())


if __name__ == '__main__':
    unittest.main()
