from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from shared.database import db
from resources.anagram import Anagram
from logging.config import dictConfig
from os import getenv

LOG_LEVEL_ALLOWED = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOG_LEVEL = getenv('ANAGRAM_LOG_LEVEL', 'INFO')

if LOG_LEVEL not in LOG_LEVEL_ALLOWED:
    LOG_LEVEL = 'INFO'

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['wsgi']
    }
})

DB_USER = getenv("ANAGRAM_DB_USER")
DB_PASS = getenv("ANAGRAM_DB_PASS")
DB_HOST = getenv("ANAGRAM_DB_HOST")
DB_PORT = getenv("ANAGRAM_DB_PORT")
DB_NAME = getenv("ANAGRAM_DB_NAME")

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{0}:{1}@{2}:{3}/{4}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(Anagram, '/anagram', '/anagram/<string:word>')

if __name__ == '__main__':
    app.run()
