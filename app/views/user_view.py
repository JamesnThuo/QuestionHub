"""Contains all the endpoints of the user functions"""

import os
import datetime
import jwt
from flask import Flask, Blueprint, request, jsonify, abort, make_response
from ..models.user import User

key = os.getenv('SECRET')
user_blue = Blueprint("user_view",__name__)

@user_blue.route('/register', methods=['POST'])
def user_signup():
    """End Point for creating User Account"""
    try:
        userdata=request.get_json()
        firstname=userdata["firstname"]
        lastname=userdata["lastname"]
        email=userdata["email"]
        password=userdata["password"]
    except Exception:
        return jsonify({
           "error" : "invalid user data input",
           "message" : "missing either first name, second name, email or password",
           "status" : 400
         }), 400

    new_user=User([firstname, lastname, email, password])
    new_user.create_new_user()
    return jsonify({
         "status": 201, 
         "message": "user created successfully"
       }), 201
