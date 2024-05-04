import requests
import json
from flask import request, jsonify, current_app
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

load_dotenv()


class WebPageSummaryView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        JINA_PREFIX = "https://r.jina.ai/"

        data = request.get_json()
        url = data.get("url", "")

        current_app.logger.info("Request: %s", request)
        current_app.logger.info("URL: %s", url)

        try:
            response = requests.get(JINA_PREFIX + url, headers={"Accept": "application/json"})
        except Exception as e:
            print(f"Invalid URL: {url}. Error: {e}")

        response_json = json.loads(response.text)
        text_content = response_json["data"]["content"]
        # metadata = {"title": response_json["data"]["title"], "url": response_json["data"]["url"]}

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500
        )

        docs = text_splitter.create_documents([text_content])

        # TODO: rewrite to share code with yt_summary_view
        map_prompt = """
        Write a concise summary of the following:
        "{text}"
        CONCISE SUMMARY:
        """

        map_prompt_template = PromptTemplate(
            template=map_prompt, input_variables=["text"]
        )

        summary_combine_prompt = """"
        Write detailed and comprehensive summary of the article.
        The summary should cover the main points and key details of the text.
        Return your response in bullet points.
        ```{text}```
        BULLET POINT SUMMARY:
        """

        summary_combine_prompt_template = PromptTemplate(
            template=summary_combine_prompt, input_variables=["text"]
        )

        summary_chain = load_summarize_chain(
            llm=llm,
            chain_type="map_reduce",
            map_prompt=map_prompt_template,
            combine_prompt=summary_combine_prompt_template,
            # verbose=True
        )

        summary_output = summary_chain.run(docs)

        # TODO: add option to ask question about the text, to extend a point from summary, etc.
        return jsonify({"summary": summary_output})
