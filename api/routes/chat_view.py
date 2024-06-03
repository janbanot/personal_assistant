from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv
from datetime import datetime
from dateutil import tz  # type: ignore
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryMemory
from api.database.db_manager import DBManager

# TODO: try to implement it without using the langchain directly
load_dotenv()

context_memory = ConversationSummaryMemory(llm=ChatOpenAI(), ai_prefix="Assistant")
# TODO: refactor to use the same instance of the model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

current_datetime = datetime.now()
gmt_plus_2_tz = tz.gettz('Etc/GMT-2')
current_datetime = current_datetime.astimezone(gmt_plus_2_tz)
current_datetime_str = current_datetime.strftime('%Y/%m/%d, %H:%M:%S')

datetime_string = f"Current datetime: {current_datetime_str} \n"

template = datetime_string + """
You are an AI assistant designed for ultra-concise, engaging conversations.
Follow these rules:
- Use the fewest words possible while maintaining clarity, impact and natural language
- Keep a friendly, casual tone with occasional colloquialisms
- Always wrap code with triple backticks and keywords with `single backticks`
- Ask for clarification to avoid assumptions
- Detect intentions and emotional states to tailor responses perfectly.
- Focus solely on instructions and provide relevant, comprehensive responses
- Never repeat info or mention limitations
- Simplify complex tasks; provide the best output possible
- Prioritize user needs; tailor responses to their context and goals
- When asked for specific content, start response with requested info immediately
- Continuously improve based on user feedback

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

    def __init__(self):
        self.db_manager = DBManager()

    def post(self):
        data = request.get_json()
        input_text = data.get("message", "")
        conversation_id = data.get("conversation_id", "")
        # TODO: buffer or context_memory?
        current_context = context_memory.buffer

        result = conversation.predict(input=input_text)

        self.db_manager.save_message(conversation_id, input_text, current_context, result)

        return jsonify({"message": result})
