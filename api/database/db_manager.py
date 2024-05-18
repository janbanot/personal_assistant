from api.database.models.chat_history import ChatHistory
from api.extensions import db


class DBManager:
    def save_message(self, conversation_id, user_message, current_context, answer):
        new_message = ChatHistory(
            conversation_id=conversation_id,
            user_message=user_message,
            current_context=current_context,
            answer=answer,
        )
        db.session.add(new_message)
        db.session.commit()

    def get_messages_by_conversation(self, conversation_id):
        messages = (
            db.session.query(ChatHistory)
            .filter(ChatHistory.conversation_id == conversation_id)
            .all()
        )
        return messages
