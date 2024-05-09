from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.database.models.chat_history import ChatHistory


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ChatHistory
        fields = ("message_id", "conversation_id", "user_message", "current_context", "answer")
