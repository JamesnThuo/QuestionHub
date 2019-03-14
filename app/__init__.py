import os
import psycopg2
from instance.config import app_config
from flask import Flask, Blueprint, jsonify

def create_app(name_conf):
    # We will be using the config variable to determine the database
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[name_conf])
    app.config.from_pyfile('config.py')
    # db_url = app_config[name_conf].Database_Url

    return app