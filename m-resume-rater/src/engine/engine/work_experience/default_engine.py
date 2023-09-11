from queue import Queue
from threading import Thread

from src.rate import Rate
from src.model import Model
from src.resume import Entity
from src.conversation.shutdown_request import ShutdownRequest
from src.conversation.engine.request import Request
from src.conversation.engine.response import Response


# todo -- to test it + think about base-class
class Engine:
    ENTITY = Entity.WORK_EXPERIENCE
    LABEL = 'default'
    NAME = 'DEFAULT WORK EXPERIENCE ENGINE'

    def __init__(self,
                 q__input: Queue,
                 q__conductor: Queue,
                 model: Model) -> None:
        self._q__input = q__input
        self._q__conductor = q__conductor
        self._model = model

    def next_item(self):
        return self._q__input.get()

    def execute(self, request: Request):
        result = self._model.execute(request.part)
        description = self._create_description(result[1])
        rate = Rate(self.ENTITY, self.LABEL, result[0], description)
        self._q__conductor.put(Response(request.idx, request.resume_id, rate))

    @staticmethod
    def _create_description(raw: tuple) -> str:
        result = ''
        for item in reversed(raw):
            score, part, task = item
            result += f'*{score:.4f}*\n  *Found*: {part}\n  *Task*: {task}\n'
        return result


def consume(engine: Engine) -> None:
    print(f'\n[{engine.NAME}] is started.')

    while True:
        item = engine.next_item()
        if isinstance(item, ShutdownRequest):
            break
        elif isinstance(item, Request):
            engine.execute(item)

    print(f'\n[{engine.NAME}] is done.')


def start_engine(q__input: Queue,
                 q__conductor: Queue,
                 model: Model) -> None:
    engine = Engine(q__input, q__conductor, model)
    consumer = Thread(target=consume, args=(engine,))
    consumer.start()


# todo del
if __name__ == '__main__':
    import time
    import torch
    from sentence_transformers import SentenceTransformer, util
    from src.resume import Part
    from src.utils import NWordsComputer, get_torch_device
    from src.model.corpus import Corpus
    from src.utils.kwargs_util import check_type_and_get_or_default, ArgDescription
    from src.utils.limited_sorted_holder import Holder
    from src.resume import Id as ResumeId, Entity
    from src.adaptation.adapter.adapter import Adapter
    from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\corpus\\dev_corpus.txt'
    pretrained_path = 'sentence-transformers/LaBSE'

    threshold_ = 0.0

    embedder_ = SentenceTransformer(pretrained_path)
    embedder_.to(get_torch_device())
    corpus_ = Corpus.create(path, embedder_).value
    computer_ = NWordsComputer()
    model_ = Model(embedder_, corpus_, computer_)

    path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
    with open(path, 'r', encoding='utf-8') as file:
        content_ = file.read()

    adapter_ = Adapter()
    adapter_.extractor(Entity.WORK_EXPERIENCE, extract_work_experience_from_hh)

    resume_ = adapter_.compute_resume(ResumeId.url('https://10.0.0.1').value, content_)
    part_ = resume_.get(Entity.WORK_EXPERIENCE)

    q_input = Queue(100)
    q_conductor = Queue(100)
    print(q_conductor)

    start_engine(q_input, q_conductor, model_)

    request_ = Request(123, resume_.resume_id, part_)
    q_input.put(request_)

    # time.sleep(5)
    # print(q_conductor.qsize())
    # if q_conductor.qsize() > 0:
    response = q_conductor.get()
    print(f'response: {response}')

    q_input.put(ShutdownRequest())
