from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from api.database.db_manager import DBManager


class DBConversationIdView(MethodView):
    decorators = [jwt_required()]

    def __init__(self):
        self.db_manager = DBManager()

    def get(self):
        conversation_id = self.db_manager.get_current_conversation_id()
        return jsonify({"conversation_id": conversation_id})
