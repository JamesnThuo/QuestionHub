"""Endpoints for upvote mdoel"""
from flask import Flask, Blueprint, make_response,jsonify, request, abort
from ..models.upvote import Upvote

upvote_blue=Blueprint("upvote_view",__name__)

@upvote_blue.route("/<question_id>/answers/<answer_id>",methods=['POST'])
def add_upvote(question_id,answer_id):
    """Endpoint for upvoting an answer"""
    try:
        upvote_data=request.get_json()
        answer_id=answer_id
        user_id=upvote_data['user_id']
    except Exception:
        return jsonify({
           "error" : "invalid upvote data input",
           "message" : "missing user id",
           "status" : 400
        }), 400
    add_upvote=Upvote([answer_id,user_id])
    add_upvote.add_upvote()
    return jsonify({
         "status": 201, 
         "message": "Upvote added successfully"
       }), 201
