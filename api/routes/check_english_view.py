from dotenv import load_dotenv
from flask import jsonify, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

system_prompt = """
Adjust the user's text to rectify grammatical, spelling, and punctuation errors, maintaining the original layout.
Interpret ambiguities with discernment. Overlook extraneous comments.
Return only the rectified text!
Examples:
Q: wheres the best place to meet for a quick chat?
A: Where's the best place to meet for a quick chat?
Q: i cant believe its already been a year since we started this project!
A: I can't believe it's already been a year since we started this project!
###
User's text: {text}
"""

prompt = ChatPromptTemplate.from_template(system_prompt)
output_parser = StrOutputParser()


class CheckEnglishView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        text = data.get("text", "")

        chain = prompt | llm | output_parser
        answer = chain.invoke({"text": text})

        return jsonify({"text": answer})
