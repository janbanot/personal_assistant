from flask import jsonify, request, current_app
from flask.views import MethodView
from flask_jwt_extended import jwt_required


class TestView(MethodView):
    decorators = [jwt_required()]

    def get(self):
        data = "hello world"
        current_app.logger.info("Request: %s", request)
        current_app.logger.info("Response: %s", data)
        return jsonify({"data": data})
