import os
import flask
import telebot

from telebot import TeleBot
from flask import Flask, request, Response
from queue import Queue
from sentence_transformers import SentenceTransformer

from src.conversation.shutdown_request import ShutdownRequest
from src.resume import Entity
from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh
from src.adaptation.adapter.adapter import Adapter
from src.model.model import Model
from src.controller.bot_controller import start_controller
from src.engine.conductor.conductor import start_conductor
from src.engine.engine.work_experience.default_engine import start_engine
from src.utils.torch_device import get_torch_device
from src.utils.nwords_computer import NWordsComputer
from src.model.corpus import Corpus
from src.bot.engine.engine import Engine
from src.bot.message.determinant.chain import Chain
from src.bot.message.determinant.determinant import (
    AnyCommandDeterminant,
    SpecificCommandDeterminant,
    TextDeterminant
)
from src.bot.engine.strategy import (
    StartCommandEngineStrategy
)
from src.bot.user import Users


TOKEN_VAR_NAME = 'DEV_TELEGRAM_BOT_TOKEN'
HOST = 'localhost'
PORT = 5000
FLASK_ABORT_CODE = 403
ROUTE_RULE = '/'
ROUTE_METHODS = ['POST', 'GET']
ENCODING = 'utf-8'

CORPUS_PATH = 'C:\\Users\\KasymbekovPN\\projects\\_temporary\\corpus\\dev_corpus.txt'
PREPARED_PATH = 'sentence-transformers/LaBSE'


def run():
    embedder = SentenceTransformer(PREPARED_PATH)
    embedder.to(get_torch_device())
    corpus = Corpus.create(CORPUS_PATH, embedder).value
    computer = NWordsComputer()

    model = Model(embedder, corpus, computer)
    q_controller = Queue(1_000)
    q_conductor = Queue(1_000)
    q_we_engine_default = Queue(1_000)

    adapter = Adapter()
    adapter.extractor(Entity.WORK_EXPERIENCE, extract_work_experience_from_hh)

    chain = Chain([
        SpecificCommandDeterminant('/start', StartCommandEngineStrategy()),
        AnyCommandDeterminant(),
        TextDeterminant(adapter)
    ])

    token = os.environ.get(TOKEN_VAR_NAME)
    bot = TeleBot(token)

    users = Users()

    engine = Engine(bot, chain, users)

    controller = start_controller(q_controller, q_conductor, engine, users)
    start_engine(q_we_engine_default, q_conductor, model)
    start_conductor(q_conductor, q_controller, q__work_experience__default=q_we_engine_default)

    app = Flask(__name__)

    def flask_abort():
        flask.abort(FLASK_ABORT_CODE)

    @app.route(ROUTE_RULE, methods=ROUTE_METHODS)
    def index():
        if request.headers.get('content-type') == 'application/json':
            update = telebot.types.Update.de_json(
                request.stream.read().decode(ENCODING)
            )
            controller.handle_update(update)
            return ''
        flask_abort()
        return Response('ok', status=200) if request.method == 'POST' else ' '

    app.run(HOST, PORT)

    q_controller.put(ShutdownRequest())
    q_conductor.put(ShutdownRequest())
    q_we_engine_default.put(ShutdownRequest())

    print('DONE!!!')


if __name__ == '__main__':
    run()
    