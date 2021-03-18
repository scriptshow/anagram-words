from flask import Flask, make_response
from flask_restful import Api
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from shared.database import db
from shared.config import SECRET_KEY, LOG_LEVEL, LOG_LEVEL_ALLOWED, DB_NAME, DB_HOST, DB_USER, DB_PASS, DB_PORT
from resources.anagram import Anagram
from resources.user import UserSignup, UserLogin
from logging.config import dictConfig
import json

if LOG_LEVEL not in LOG_LEVEL_ALLOWED:
    LOG_LEVEL = 'INFO'

# Default logging configuration
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

# Flask configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{0}:{1}@{2}:{3}/{4}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)

# Database configuration
db.init_app(app)
migrate = Migrate(app, db)

# Manager configuration
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# API configuration
api = Api(app)
api.add_resource(Anagram, '/anagram/<string:word>', resource_class_kwargs={'secret_key': app.config['SECRET_KEY']})
api.add_resource(UserLogin, '/login', resource_class_kwargs={'secret_key': app.config['SECRET_KEY']})
api.add_resource(UserSignup, '/signup', resource_class_kwargs={'secret_key': app.config['SECRET_KEY']})


# Default output for all the request in the API
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


if __name__ == '__main__':
    manager.run()
