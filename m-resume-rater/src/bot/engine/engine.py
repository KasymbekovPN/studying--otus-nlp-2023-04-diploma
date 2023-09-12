import re

from telebot import TeleBot
from telebot.types import Update
from queue import Queue

from src.bot.message.determinant.chain import Chain
from src.bot.user import Users


class Engine:
    def __init__(self,
                 bot: TeleBot,
                 chain: Chain,
                 users: Users) -> None:
        self._bot = bot
        self._chain = chain
        self._users = users

    def handle_update(self, update: Update) -> dict:
        if update is None or update.message is None:
            return {}

        text = update.message.text
        user_id = update.message.from_user.id
        result = self._chain(text=text)

        ret = result.strategy.execute(user_id, result, self._bot, self._users)
        ret['user_id'] = user_id
        return ret

    def send_message(self, user_id: int, text: str, parse_mode=None) -> None:
        if parse_mode == 'Markdown':
            text = re.sub(r'_+', ' ', text)

        self._bot.send_message(user_id, text, parse_mode=parse_mode)
