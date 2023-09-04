import unittest

from parameterized import parameterized
from src.resume import Entity
from src.engine.conductor.conductor import Conductor, handle_init_queue_name


class TestCase(unittest.TestCase):

    @parameterized.expand([
        ('q__cv__default', Entity.CV, 'default', True),
        ('q__education__default', Entity.EDUCATION, 'default', True),
        ('q__refresher_courses__default', Entity.REFRESHER_COURSES, 'default', True),
        ('q__short_about__default', Entity.SHORT_ABOUT, 'default', True),
        ('q__skills__default', Entity.SKILLS, 'default', True),
        ('q__specialization__default', Entity.SPECIALIZATION, 'default', True),
        ('q__work_experience__default', Entity.WORK_EXPERIENCE, 'default', True),
        ('x__work_experience__default', None, None, False),
        ('work_experience__default', None, None, False),
        ('work_experiencedefault', None, None, False),
        ('q__work_experience', None, None, False),
        ('work_experience', None, None, False)
    ])
    def test_init_queue_name_handling(self, name: str, expected_entity, expected_label, expected_success: bool):
        success, entity, label = handle_init_queue_name(name)
        self.assertTupleEqual((success, entity, label), (expected_success, expected_entity, expected_label))


if __name__ == '__main__':
    unittest.main()
