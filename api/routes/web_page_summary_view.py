from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from dotenv import load_dotenv

load_dotenv()


class WebPageSummaryView(MethodView):
    decorators = [jwt_required()]

    def post(self):
        data = request.get_json()
        return jsonify({"message": data})
