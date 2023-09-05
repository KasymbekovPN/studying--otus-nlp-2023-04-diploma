from queue import Queue
from threading import Thread

from src.resume import Resume, Part, Id as ResumeId
from src.conversation.conductor.request import Request
from src.conversation.conductor.response import Response
from src.conversation.shutdown_request import ShutdownRequest


class FakeController:
    LINES = [
        """Встраиваемых терминалов защит, которые осуществляют контроль токовых и напряженческих параметров,
        управление контакторами на 690, 1140, 6000 В; защиты по току и напряжению, АГЗ, внешние защиты и пр.""",
        'Блок индикации и настройки терминала защит.',
        'Блок измерения температур',
        'Устройство плавного пуска',
        'Устройство сбора и хранения информации(по CAN)'
    ]

    def __init__(self,
                 q__input: Queue,
                 q__conductor: Queue) -> None:
        self._q_input = q__input
        self._q_conductor = q__conductor

    # todo: it's temporary solution
    def send(self):
        resume = Resume(ResumeId.url('https://10.0.0.1').value, work_experience=Part(*self.LINES))
        self._q_conductor.put(Request(123, resume))

    def next_item(self):
        return self._q_input.get()

    # todo !!!
    def apply_response(self, response: Response):
        print(f'!!! response: {response}')


def consume(controller: FakeController) -> None:
    print(f'\nFakeController is started.')

    while True:
        item = controller.next_item()
        if isinstance(item, ShutdownRequest):
            break
        elif isinstance(item, Response):
            controller.apply_response(item)

    print(f'\nFakeController is done.')


def start_controller(q__input: Queue,
                     q__conductor: Queue) -> FakeController:
    controller = FakeController(q__input, q__conductor)
    consumer = Thread(target=consume, args=(controller,))
    consumer.start()

    return controller
