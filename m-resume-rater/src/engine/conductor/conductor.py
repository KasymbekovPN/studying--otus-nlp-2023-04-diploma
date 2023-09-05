from queue import Queue
from threading import Thread

from src.resume import Entity
from src.conversation.shutdown_request import ShutdownRequest
from src.conversation.conductor.request import Request as ConductorRequest
from src.conversation.conductor.response import Response as ConductorResponse
from src.conversation.engine.request import Request as EngineRequest
from src.conversation.engine.response import Response as EngineResponse


def handle_init_queue_name(init_name: str) -> tuple:
    if init_name is not None:
        split_name = init_name.split('__')
        if len(split_name) == 3 and split_name[0] == 'q':
            for e in Entity:
                if e.value[1] == split_name[1]:
                    return True, e, split_name[2]
    print(f'Bad name: {init_name}')
    return False, None, None


class Conductor:
    def __init__(self,
                 q__input: Queue,
                 q__controller: Queue,
                 handler=handle_init_queue_name,
                 **kwargs):
        self._q__input = q__input
        self._q__controller = q__controller
        self._queues = {}
        self._waited = {}
        for name, queue in kwargs.items():
            success, entity, label = handler(name)
            if success:
                if entity not in self._queues:
                    self._queues[entity] = {}
                self._queues[entity][label] = queue

    def next_item(self):
        return self._q__input.get()

    def send_request(self, request: ConductorRequest) -> None:
        s = set()
        for entity, queues_by_labels in self._queues.items():
            resume = request.resume
            part = resume.get(entity)
            for label, queue in queues_by_labels.items():
                s.add(f'{entity.value[1]}_{label}')# todo method
                queue.put(EngineRequest(request.idx, resume.resume_id, part))
        self._waited[request.idx] = s

    def receive_response(self, response: EngineResponse) -> None:
        idx = response.idx
        sid = f'{response.entity.value[1]}_{response.label}'# todo method
        if idx in self._waited:
            self._waited[idx].remove(sid)
            if len(self._waited[idx]) == 0:
                del self._waited[idx]
                self._q__controller.put(ConductorResponse(idx, response.resume_id, response.rate))


def consume(conductor: Conductor):
    print('\nCONDUCTOR is started.')

    while True:
        item = conductor.next_item()
        if isinstance(item, ShutdownRequest):
            break
        elif isinstance(item, ConductorRequest):
            conductor.send_request(item)
        elif isinstance(item, EngineResponse):
            conductor.receive_response(item)

    print('\nCONDUCTOR is done.')


def start_conductor(q__input: Queue,
                    q__controller: Queue,
                    **kwargs):
    conductor = Conductor(q__input, q__controller, **kwargs)
    consumer = Thread(target=consume, args=(conductor,))
    consumer.start()
