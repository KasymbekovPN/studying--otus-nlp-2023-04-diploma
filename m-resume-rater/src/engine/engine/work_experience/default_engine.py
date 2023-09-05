from queue import Queue
from threading import Thread

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
        rate = self._model.execute(request.part)
        self._q__conductor.put(Response(request.idx, request.resume_id, rate, self.ENTITY, self.LABEL))


def consume(engine: Engine) -> None:
    print(f'\n[{engine.NAME}] is started.')

    while True:
        item = engine.next_item()
        if isinstance(item, ShutdownRequest.__class__):
            break
        elif isinstance(item, Request.__class__):
            engine.execute(item)

    print(f'\n[{engine.NAME}] is done.')


def start_engine(q__input: Queue,
                 q__conductor: Queue,
                 model: Model) -> None:
    engine = Engine(q__input, q__conductor, model)
    consumer = Thread(target=consume, args=(engine,))
    consumer.start()
