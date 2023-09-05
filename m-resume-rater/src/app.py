from flask import Flask, request
from queue import Queue

from src.model.model import Model
from src.controller.fake_controller import start_controller
from src.engine.conductor.conductor import start_conductor
from src.engine.engine.work_experience.default_engine import start_engine


HOST = 'localhost'
PORT = 5000
FLASK_ABORT_CODE = 403
ROUTE_RULE = '/'
ROUTE_METHODS = ['POST', 'GET']


def run():
    model = Model()
    q_controller = Queue(1_000)
    q_conductor = Queue(1_000)
    q_we_engine_default = Queue(1_000)

    controller = start_controller(q_controller, q_conductor)
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
    