from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI

load_dotenv()

check_english = Blueprint("check_english", __name__)

# TODO: check if I can initialize the model globally not every time the route is called
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

template = """
"""


@check_english.route("/check-english", methods=["POST"])
@jwt_required()
def check_english_route():
    data = request.get_json()
    return jsonify({"message": f"Not implemented yet {data}"})
