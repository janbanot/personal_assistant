import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

check_english = Blueprint("check_english", __name__)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_key)

template = """
"""


@check_english.route("/check-english", methods=["POST"])
@jwt_required()
def check_english_route():
    data = request.get_json()
    return jsonify({"message": f"Not implemented yet {data}"})
