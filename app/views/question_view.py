"""Contains the endpoints for Question Model"""
import os
from flask import Flask, Blueprint, request, jsonify, abort, make_response
from ..models.question import Question

question_blue=Blueprint("question_view",__name__)

@question_blue.route("/questions", methods=['POST'])
def add_question():
    """Endpoint for adding question"""
    try:
        questiondata=request.get_json()
        description=questiondata['description']
        user_id=questiondata['user_id']
    except Exception:
        return jsonify({
           "error" : "invalid question data input",
           "message" : "missing either question or user id",
           "status" : 400
        }),400
    new_question=Question([description,user_id])
    new_question.add_question()
    return jsonify({
         "status": 201, 
         "message": "Question added successfully"
       }), 201
    

    


