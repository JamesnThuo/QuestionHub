"""Contains endpoints for the question model"""
from flask import Flask,Blueprint,jsonify,request,make_response, abort
from ..models.answer import Answer

answer_blue=Blueprint("answer_view", __name__)

@answer_blue.route('/<question_id>/answers',methods=['POST'])
def add_quesion(question_id):
    """Endpoint for adding answer"""
    try:
        answer_data=request.get_json()
        description=answer_data['description']
        questionid=question_id
    except Exception:
        return jsonify({
           "error" : "invalid answer data input",
           "message" : "missing answer",
           "status" : 400
        }), 400
    new_answer=Answer([description,questionid])
    new_answer.add_answer()
    return jsonify({
         "status": 201, 
         "message": "Answer added successfully"
       }), 201