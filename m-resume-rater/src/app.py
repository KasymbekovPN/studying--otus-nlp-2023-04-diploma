from flask import Flask, request
from queue import Queue
from sentence_transformers import SentenceTransformer

from src.resume import Entity
from src.adaptation.extractor.hh.work_experience.extractor import extract_work_experience_from_hh
from src.adaptation.adapter.adapter import Adapter
from src.model.model import Model
from src.controller.fake_controller import start_controller
from src.engine.conductor.conductor import start_conductor
from src.engine.engine.work_experience.default_engine import start_engine
from src.utils.torch_device import get_torch_device
from src.utils.nwords_computer import NWordsComputer
from src.model.corpus import Corpus


HOST = 'localhost'
PORT = 5000
FLASK_ABORT_CODE = 403
ROUTE_RULE = '/'
ROUTE_METHODS = ['POST', 'GET']

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

    controller = start_controller(q_controller, q_conductor, adapter)
    start_engine(q_we_engine_default, q_conductor, model)
    start_conductor(q_conductor, q_controller, q__work_experience__default=q_we_engine_default)

    app = Flask(__name__)

    @app.route(ROUTE_RULE, methods=ROUTE_METHODS)
    def index():
        controller.send()
        return ''

    app.run(HOST, PORT)


if __name__ == '__main__':
    run()
    