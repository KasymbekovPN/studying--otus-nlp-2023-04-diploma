import unittest

from parameterized import parameterized
from src.resume import Id as ResumeId, Entity
from src.rate import Rate
from src.conversation.engine.response import Response


class TestCase(unittest.TestCase):
    _IDX = 123
    _RESUME_ID = ResumeId.url('https://10.0.0.1').value
    _RATE = Rate(Entity.WORK_EXPERIENCE, 'default')

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
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                None,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                123,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(2, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(1, ResumeId.url('https://10.0.0.2').value, Rate(Entity.CV, 'default')),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default1')),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.SKILLS, 'default')),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default1')),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(Entity.CV, 'default')),
                True
        )
    ])
    def test_response_eq(self, first: Response, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_response_repr(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE)
        expected = f'Response {{id: {self._IDX}, resume_id: {self._RESUME_ID}, entity: {self._RATE.entity}, label: {self._RATE.label} }}'

        self.assertEqual(expected, response.__repr__())


if __name__ == '__main__':
    unittest.main()
