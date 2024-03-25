import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

if openai_key is None:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables")

chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_key)

template = """The following is a conversation between a human and an AI personal assistant.
The Assistant provide clear and concise answers to the with minimum unnecessary information.
If the Assistant does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}
AI Assistant:
"""

PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)
context_memory = ConversationSummaryMemory(llm=ChatOpenAI(), ai_prefix="Assistant")
conversation = ConversationChain(
    prompt=PROMPT,
    llm=chat_model,
    verbose=True,
    memory=context_memory,
)

chat = Blueprint('chat', __name__)
clear = Blueprint('clear', __name__)


@chat.route('/chat', methods=['POST'])
@jwt_required()
def chat_route():
    data = request.get_json()
    input_text = data.get('message', '')
    # TODO: figure out out to handle memory clearing to have a new conversation with new context
    # context_memory.clear()
    result = conversation.predict(input=input_text)
    return jsonify({"message": result})


@clear.route('/clear-context', methods=['POST'])
@jwt_required()
def clear_route():
    context_memory.clear()
    return jsonify({"message": "Context memory cleared"})
