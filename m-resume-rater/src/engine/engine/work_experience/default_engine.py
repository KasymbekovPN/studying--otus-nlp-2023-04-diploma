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
