from flask import Flask, request


HOST = 'localhost'
PORT = 5000
FLASK_ABORT_CODE = 403
ROUTE_RULE = '/'
ROUTE_METHODS = ['POST', 'GET']


def run():
    app = Flask(__name__)

    @app.route(ROUTE_RULE, methods=ROUTE_METHODS)
    def index():
        x = request
        print(x)
        return ''

    app.run(HOST, PORT)


if __name__ == '__main__':
    run()
    