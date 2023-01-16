from flask import Flask
from flask_restful import Api
from plate.generate import Generate


app = Flask(__name__)
api = Api()



api.add_resource(Generate, '/api/plate/generate/<int:amount>')
api.init_app(app)


if __name__ == '__main__':
    app.run(port=3000, host='127.0.0.1')