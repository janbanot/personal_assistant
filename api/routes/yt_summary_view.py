from flask import request, jsonify, current_app
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


class YTSummaryView(MethodView):
    decorators = [jwt_required()]

    # TODO: make the summary longer, add option to get bullet points
    def post(self):
        data = request.get_json()
        url = data.get("url", "")

        current_app.logger.info("Request: %s", request)
        current_app.logger.info("URL: %s", url)

        try:
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        except Exception as e:
            print(f"Invalid YouTube URL: {url}. Error: {e}")
        result = loader.load()

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
        texts = text_splitter.split_documents(result)

        # TODO: check how to improve the summarization https://python.langchain.com/docs/use_cases/summarization/
        chain = load_summarize_chain(llm=llm, chain_type="map_reduce", verbose=False)

        summary = chain.run(texts)

        current_app.logger.info("Summary: %s", summary)

        return jsonify({"summary": summary})
