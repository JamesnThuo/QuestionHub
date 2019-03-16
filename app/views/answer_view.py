"""Contains endpoints for the question model"""
from flask import Flask,Blueprint,jsonify,request,make_response, abort
from ..models.answer import Answer

answer_blue=Blueprint("answer_view", __name__)

@answer_blue.route('/<question_id>/answers')
def add_quesion(question_id):
    return None