"""Contains the endpoints for Question Model"""
import os
from flask import Flask, Blueprint, request, jsonify, abort, make_response
from ..models.question import Question

question_blue=Blueprint("view",__name__)

@question_blue.route("/question", methods=['POST'])
def add_question():
    """Endpoint for adding question"""
    try:
        questiondata=request.get_json()
        description=questiondata['question']
        user_id=questiondata['user_id']
    except Exception:
        return jsonify({
           "error" : "invalid question data input",
           "message" : "missing either question or user id",
           "status" : 400
        }),400
    new_question=Question(questiondata)
    new_question.add_question()
    

    


