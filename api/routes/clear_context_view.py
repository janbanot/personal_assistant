from flask import jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from api.routes.chat_view import context_memory


class ClearView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        context_memory.clear()
        return jsonify({"message": "Context memory cleared"})
