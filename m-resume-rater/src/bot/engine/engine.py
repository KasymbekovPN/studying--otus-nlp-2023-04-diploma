from telebot import TeleBot
from telebot.types import Update
from queue import Queue

from src.bot.message.determinant.chain import Chain
from src.bot.user import Users


class Engine:
    def __init__(self,
                 q_input: Queue,
                 bot: TeleBot,
                 chain: Chain,
                 users: Users) -> None:
        self._q_input = q_input
        self._bot = bot
        self._chain = chain
        self._users = users

    def set_update(self, update: Update):
        if update is None or update.message is None:
            return

        text = update.message.text
        user_id = update.message.from_user.id
        result = self._chain(text=text)

        result.strategy.execute(user_id, result, self._bot, self._q_input, self._users, update)
