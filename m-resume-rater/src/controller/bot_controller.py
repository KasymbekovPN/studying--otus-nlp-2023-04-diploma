from queue import Queue
from threading import Thread

from telebot.types import Update
from src.bot.user import Users, UserState
from src.conversation.conductor.response import Response
from src.conversation.shutdown_request import ShutdownRequest
from src.bot.engine.engine import Engine


class BotController:
    def __init__(self,
                 q__input: Queue,
                 q__conductor: Queue,
                 bot_engine: Engine,
                 users: Users) -> None:
        self._q_input = q__input
        self._q_conductor = q__conductor
        self._bot_engine = bot_engine
        self._user_ids = {}
        self._users = users

    def handle_update(self, update: Update):
        ret = self._bot_engine.handle_update(update, self._q_conductor)
        if 'user_id' in ret and 'request_id' in ret:
            self._user_ids[ret['request_id']] = ret['user_id']

    def next_item(self):
        return self._q_input.get()

    def apply_response(self, response: Response):
        idx = response.idx
        if idx in self._user_ids:
            user_id = self._user_ids[idx]
            self._users.get(user_id).state = UserState.INIT
            del self._user_ids[idx]

            for message in self._create_messages(response):
                self._bot_engine.send_message(user_id, message, parse_mode="Markdown")

    @staticmethod
    def _create_messages(response: Response) -> tuple:
        messages = []
        for entity, value in response.rates.rates.items():
            for label, rate in value.items():
                message = f'*Request ID*: {response.idx}\n'
                message += f'*Resume*: {response.resume_id.value}\n'
                message += f'*Entity*: {entity.value[1]}\n'
                message += f'*Label*: {label}\n'
                message += f'*Score*: {rate.value:.4f}\n\n'
                message += f'*Description*:\n{rate.description}\n'
                messages.append(message)

        return tuple(messages)


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
                     bot_engine: Engine,
                     users: Users) -> BotController:
    controller = BotController(q__input, q__conductor, bot_engine, users)
    consumer = Thread(target=consume, args=(controller,))
    consumer.start()

    return controller
