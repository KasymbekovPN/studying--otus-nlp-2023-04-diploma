import unittest

from queue import Queue
from parameterized import parameterized
from src.rate import Rate
from src.resume import Entity, Resume, Id as ResumeId, Part
from src.engine.conductor.conductor import Conductor, handle_init_queue_name
from src.conversation.conductor.request import Request as ConductorRequest
from src.conversation.conductor.response import Response as ConductorResponse
from src.conversation.engine.request import Request as EngineRequest
from src.conversation.engine.response import Response as EngineResponse


class TestCase(unittest.TestCase):

    class TestQueue(Queue):
        def __init__(self):
            super().__init__()
            self.item = None

        def put(self, item, block=True, timeout=None) -> None:
            self.item = item

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

    def test_next_item(self):
        expected_item = 'some.item'
        queue = Queue(maxsize=10)
        queue.put(expected_item)

        conductor = Conductor(queue, Queue())
        item = conductor.next_item()
        self.assertEqual(expected_item, item)

    def test_send_request(self):
        request_id = 123
        cv_part = Part('cv.part')
        education_part = Part('education.part')
        resume_id = ResumeId.url('https://10.0.0.1').value
        resume = Resume(resume_id, cv=cv_part, education=education_part)
        request = ConductorRequest(request_id, resume)
        expected_waited = {request_id: {'cv_default', 'education_default'}}

        q_cv = TestCase.TestQueue()
        q_education = TestCase.TestQueue()
        conductor = Conductor(Queue(), Queue(), q__cv__default=q_cv, q__education__default=q_education)
        conductor.send_request(request)

        self.assertEqual(expected_waited, conductor._waited)
        self.assertEqual(EngineRequest(request_id, resume_id, cv_part), q_cv.item)
        self.assertEqual(EngineRequest(request_id, resume_id, education_part), q_education.item)

    def test_receive_response(self):
        pass
        # todo restore
        # request_id = 123
        # resume_id = ResumeId.url('https://10.0.0.1').value
        # rate = Rate()
        # q_collector = TestCase.TestQueue()
        # q_input = Queue()
        # conductor = Conductor(q_input, q_collector)
        # conductor._waited = {request_id: {'cv_default', 'education_default'}}
        #
        # conductor.receive_response(EngineResponse(request_id, resume_id, rate, Entity.CV, 'default'))
        # conductor.receive_response(EngineResponse(request_id, resume_id, rate, Entity.EDUCATION, 'default'))
        #
        # self.assertEqual(ConductorResponse(request_id, resume_id, rate), q_collector.item)


if __name__ == '__main__':
    unittest.main()
