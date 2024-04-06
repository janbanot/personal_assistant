import os
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

yt_summary = Blueprint("yt_summary", __name__)


@yt_summary.route("/yt-summary", methods=["POST"])
@jwt_required()
def yt_summary_route():
    data = request.get_json()
    url = data.get("url", "")

    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
    result = loader.load()

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=openai_key)

    # TODO: test with diffrent params chere and in chain as well
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_documents(result)

    chain = load_summarize_chain(llm=llm, chain_type="map_reduce", verbose=False)

    summary = chain.run(texts)

    return jsonify({"summary": summary})
