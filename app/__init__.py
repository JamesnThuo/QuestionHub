import os
from .models.database import DatabaseConnection
from instance.config import app_config
from flask import Flask, Blueprint, jsonify
from .views.user_view import user_blue
from .views.question_view import question_blue

def create_app(name_conf):
    # We will be using the config variable to determine the database
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_object(app_config[name_conf])
    app.config.from_pyfile('config.py')
    db_url = app_config[name_conf].Database_Url
    
    print("\n\n\n", db_url, "\n\n\n")

    DatabaseConnection(db_url)
    if name_conf=="testing":
        DatabaseConnection.drop_tables(DatabaseConnection)
    DatabaseConnection.create_tables(DatabaseConnection)
    
    app.register_blueprint(user_blue, url_prefix="/api/user")
    app.register_blueprint(question_blue, url_prefix="/api")
    return app