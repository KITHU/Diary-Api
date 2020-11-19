# system import
from os import getenv

# third party import
from flask import jsonify

# local import
from main import create_app
from config import config


# get flask config name from env or default to production config
config_name = getenv('FLASK_ENV', default='production')

# create application object
app = create_app(config[config_name])

@app.route('/')
def index():
    """Process / routes and returns 'Welcome to the AM api' as json."""
    return jsonify(dict(message='Welcome to my api'))


if __name__ == '__main__':
    app.run()
