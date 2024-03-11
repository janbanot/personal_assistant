from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

chat = Blueprint('chat', __name__)


@chat.route('/chat', methods=['GET'])
@jwt_required()
def chat_route():
    return jsonify({"message": "Here will be conversation with chatbot."})
