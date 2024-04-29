from dotenv import load_dotenv
from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

template = """
"""


class CheckEnglishView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        return jsonify({"message": f"Not implemented yet {data}"})
