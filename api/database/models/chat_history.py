from sqlalchemy import Column, Integer, String
from api.extensions import db


class ChatHistory(db.Model):  # type: ignore
    __tablename__ = "chat_history"
    message_id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer)
    user_message = Column(String)
    current_context = Column(String)
    answer = Column(String)
