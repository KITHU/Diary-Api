import os
import pytest

#local import
from main import create_app
from config import config

config_name = 'testing'
os.environ['FLASK_ENV'] = config_name

def client():
    create_app(config=config.get(config_name))
