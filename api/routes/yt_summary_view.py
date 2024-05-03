from flask import request, jsonify, current_app
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


class YTSummaryView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        url = data.get("url", "")

        current_app.logger.info("Request: %s", request)
        current_app.logger.info("URL: %s", url)

        try:
            loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        except Exception as e:
            print(f"Invalid YouTube URL: {url}. Error: {e}")
        results = loader.load()

        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500
        )

        for document in results:
            text_content = document.page_content

        docs = text_splitter.create_documents([text_content])

        map_prompt = """
        Write a concise summary of the following:
        "{text}"
        CONCISE SUMMARY:
        """

        map_prompt_template = PromptTemplate(
            template=map_prompt, input_variables=["text"]
        )

        summary_combine_prompt = """
        Please provide a detailed and comprehensive summary of the video transcript text.
        The summary should capture the main points and key details of the text while conveying the author's intended meaning accurately.
        Second part should be a bulletpoint summary of the text.

        Example:
        In the video, the author discusses creating a chatbot that reads AI news from different sources using Gradient AI's hosted retrieval solution.
        They demonstrate how to build the chatbot in a few lines of code and deploy it on Streamlit for easy access.

        - The author created a chatbot that reads AI news from different sources
        - The chatbot uses Gradient AI's hosted retrieval solution to answer user queries
        - The chatbot was built in a few lines of code and deployed on Streamlit for easy access

        ```{text}```
        SUMMARY:
        """  # noqa
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

        return jsonify({"summary": summary_output})
