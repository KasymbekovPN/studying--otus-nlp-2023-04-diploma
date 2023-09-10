from queue import Queue
from threading import Thread

from telebot.types import Update
from src.resume import Resume, Part, Id as ResumeId
from src.conversation.conductor.request import Request
from src.conversation.conductor.response import Response
from src.conversation.shutdown_request import ShutdownRequest
from src.adaptation.adapter.adapter import Adapter
from src.bot.engine.engine import Engine


class BotController:
    def __init__(self,
                 q__input: Queue,
                 q__conductor: Queue,
                 adapter: Adapter,
                 bot_engine: Engine) -> None:
        self._q_input = q__input
        self._q_conductor = q__conductor
        self._adapter = adapter
        self._bot_engine = bot_engine

    def handle_update(self, update: Update):
        # todo del
        print(update)
        self._bot_engine.handle_update(update, self._q_conductor)

        pass
        # todo !!!
        # path = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\resume5.html'
        # with open(path, 'r', encoding='utf-8') as file:
        #     content = file.read()
        #
        # resume = self._adapter.compute_resume(ResumeId.url('https://10.0.0.1').value, content)
        # self._q_conductor.put(Request(123, resume))

    def next_item(self):
        return self._q_input.get()

    # todo !!!
    def apply_response(self, response: Response):
        print(f'!!! response: {response}')
        print(f'ID: {response.idx}')
        print(f'RESUME_ID: {response.resume_id}')
        for entity, value in response.rates.rates.items():
            for label, rate in value.items():
                print(f'\n{entity.value[1]} :: {label}')
                print(f'SCORE: {rate.value}')
                print(f'{rate.description}')


def consume(controller: BotController) -> None:
    print(f'\nFakeController is started.')

    while True:
        item = controller.next_item()
        if isinstance(item, ShutdownRequest):
            break
        elif isinstance(item, Response):
            controller.apply_response(item)

    print(f'\nFakeController is done.')


def start_controller(q__input: Queue,
                     q__conductor: Queue,
                     adapter: Adapter,
                     bot_engine: Engine) -> BotController:
    controller = BotController(q__input, q__conductor, adapter, bot_engine)
    consumer = Thread(target=consume, args=(controller,))
    consumer.start()

    return controller
