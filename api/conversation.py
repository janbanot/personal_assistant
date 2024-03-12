import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0, openai_api_key=openai_key)

conversation = ConversationChain(
    llm=chat_model, verbose=True, memory=ConversationBufferMemory()
)

chat = Blueprint('chat', __name__)


@chat.route('/chat', methods=['POST'])
@jwt_required()
def chat_route():
    data = request.get_json()
    input_text = data.get('input_text', '')
    result = conversation.predict(input=input_text)
    return jsonify({"message": result})
