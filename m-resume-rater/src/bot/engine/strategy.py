import os

from telebot import TeleBot
from queue import Queue

from src.resume import Id as ResumeId
from src.bot.user import Users, UserState, User
from src.adaptation.adapter.adapter import Adapter
from src.conversation.conductor.request import Request as ConductorRequest


class BaseEngineStrategy:
    def execute(self,
                user_id: int,
                result,
                bot: TeleBot,
                users: Users) -> dict:
        bot.send_message(user_id, f'ECHO: {result}')
        return {}


class StartCommandEngineStrategy(BaseEngineStrategy):
    def execute(self,
                user_id: int,
                result,
                bot: TeleBot,
                users: Users) -> dict:
        user = users.get_or_add(user_id)
        user.state = UserState.INIT
        bot.send_message(user_id, 'Hello, I am restarted!')
        return {}


class UnknownCommandEngineStrategy(BaseEngineStrategy):
    def execute(self,
                user_id: int,
                result,
                bot: TeleBot,
                users: Users) -> dict:
        user = users.get_or_add(user_id)
        user.state = UserState.NONE
        bot.send_message(user_id, f'I do not known command {result.text}, please, enter command /start !')
        return {}


class TextEngineStrategy(BaseEngineStrategy):
    _REQUEST_COUNTER = 0

    def __init__(self, adapter: Adapter) -> None:
        self._adapter = adapter

    def execute(self,
                user_id: int,
                result,
                bot: TeleBot,
                users: Users) -> dict:
        ret = {}
        user = users.get_or_add(user_id)
        success, message = self._check_user_state(user)
        if success:
            file_path = f'C:\\Users\\KasymbekovPN\\projects\\_temporary\\resumes\\{result.text}.html'

            if os.path.isfile(file_path):
                user.state = UserState.EXEC
                message = f'Processing of {result.text} is started! REQUEST ID: {TextEngineStrategy._REQUEST_COUNTER}.'

                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                resume = self._adapter.compute_resume(ResumeId.url(f'https://{result.text}.html').value, content)

                ret['request_id'] = TextEngineStrategy._REQUEST_COUNTER
                ret['conductor_request'] = ConductorRequest(TextEngineStrategy._REQUEST_COUNTER, resume)
                TextEngineStrategy._REQUEST_COUNTER += 1
            else:
                message = f'Bad input: {result.text}'

        bot.send_message(user_id, message)
        return ret

    @staticmethod
    def _check_user_state(user: User) -> tuple:
        state = user.state
        if state == UserState.NONE:
            return False, 'The bot is not started, please, enter /start !'
        elif state == UserState.INIT:
            return True, None
        else:
            return False, 'The bot is executing resume, please, wait !'
