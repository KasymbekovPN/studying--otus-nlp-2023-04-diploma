from queue import Queue
from threading import Thread

from telebot.types import Update
from src.resume import Resume, Part, Id as ResumeId
from src.conversation.conductor.request import Request
from src.conversation.conductor.response import Response
from src.conversation.shutdown_request import ShutdownRequest
from src.bot.engine.engine import Engine


class BotController:
    def __init__(self,
                 q__input: Queue,
                 q__conductor: Queue,
                 bot_engine: Engine) -> None:
        self._q_input = q__input
        self._q_conductor = q__conductor
        self._bot_engine = bot_engine
        self._user_ids = {}

    def handle_update(self, update: Update):
        ret = self._bot_engine.handle_update(update, self._q_conductor)
        if 'user_id' in ret and 'request_id' in ret:
            self._user_ids[ret['request_id']] = ret['user_id']

    def next_item(self):
        return self._q_input.get()

    # todo !!!
    def apply_response(self, response: Response):
        idx = response.idx

        message = f'ID: {idx}\n'
        message += f'RESUME_ID: {response.resume_id}'
        for entity, value in response.rates.rates.items():
            for label, rate in value.items():
                message += f'\n{entity.value[1]} :: {label}'
                message += f'\nSCORE: {rate.value:.4f}'
                message += f'\n{rate.description}'

        # todo del
        # print(f'!!! response: {response}')
        # print(f'ID: {response.idx}')
        # print(f'RESUME_ID: {response.resume_id}')
        # for entity, value in response.rates.rates.items():
        #     for label, rate in value.items():
        #         print(f'\n{entity.value[1]} :: {label}')
        #         print(f'SCORE: {rate.value}')
        #         print(f'{rate.description}')

        if idx in self._user_ids:
            self._bot_engine.send_message(self._user_ids[idx], message)
            del self._user_ids[idx]


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
                     bot_engine: Engine) -> BotController:
    controller = BotController(q__input, q__conductor, bot_engine)
    consumer = Thread(target=consume, args=(controller,))
    consumer.start()

    return controller
