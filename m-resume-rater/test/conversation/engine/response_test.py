import unittest

from parameterized import parameterized
from src.resume import Id as ResumeId, Entity
from src.rate import Rate
from src.conversation.engine.response import Response


class TestCase(unittest.TestCase):
    _IDX = 123
    _RESUME_ID = ResumeId.url('https://10.0.0.1').value
    _RATE = Rate(1)
    _ENTITY = Entity.WORK_EXPERIENCE
    _LABEL = 'default'

    def test_response_idx_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        self.assertEqual(self._IDX, response.idx)

    def test_response_resume_id_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        self.assertEqual(self._RESUME_ID, response.resume_id)

    def test_response_rate_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        self.assertEqual(self._RATE, response.rate)

    def test_response_entity_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        self.assertEqual(self._ENTITY, response.entity)

    def test_response_label_getting(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        self.assertEqual(self._LABEL, response.label)

    @parameterized.expand([
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                None,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                123,
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(2, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(1, ResumeId.url('https://10.0.0.2').value, Rate(1), Entity.CV, 'default'),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(2), Entity.CV, 'default'),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.SKILLS, 'default'),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default1'),
                False
        ),
        (
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                Response(1, ResumeId.url('https://10.0.0.1').value, Rate(1), Entity.CV, 'default'),
                True
        )
    ])
    def test_response_eq(self, first: Response, second, expected: bool):
        self.assertEqual(expected, first.__eq__(second))

    def test_response_repr(self):
        response = Response(self._IDX, self._RESUME_ID, self._RATE, self._ENTITY, self._LABEL)
        expected = f'Response {{id: {self._IDX}, resume_id: {self._RESUME_ID}, entity: {self._ENTITY}, label: {self._LABEL} }}'

        self.assertEqual(expected, response.__repr__())


if __name__ == '__main__':
    unittest.main()
