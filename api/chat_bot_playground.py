import dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser

dotenv.load_dotenv()

review_template_str = """You are a personal assistant.
Use the following context to answer questions.
Be as detailed as possible If you don't know an answer, say
you don't know.

{context}
"""

review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"],
        template=review_template_str,
    )
)

review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["question"],
        template="{question}",
    )
)
messages = [review_system_prompt, review_human_prompt]

review_prompt_template = ChatPromptTemplate(
    input_variables=["context", "question"],
    messages=messages,  # type: ignore
)

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)  # type: ignore

output_parser = StrOutputParser()

review_chain = review_prompt_template | chat_model | output_parser
