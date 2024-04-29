from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory

load_dotenv()

context_memory = ConversationSummaryMemory(llm=ChatOpenAI(), ai_prefix="Assistant")
# TODO: refactor to use the same instance of the model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

template = """The following is a conversation between a human and an AI personal assistant.
The Assistant provide clear and concise answers to the with minimum unnecessary information.
If the Assistant does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}
AI Assistant:
"""

# TODO: Check why langchain default template example is sent in the context with every message?
PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

conversation = ConversationChain(
    prompt=PROMPT,
    llm=llm,
    verbose=True,
    memory=context_memory,
)


class ChatView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        input_text = data.get("message", "")
        result = conversation.predict(input=input_text)
        return jsonify({"message": result})
