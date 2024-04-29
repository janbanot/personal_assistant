from flask import jsonify, request
from flask.views import MethodView
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from api.models.user import User
# from api.models.user_schema import UserSchema


class LoginView(MethodView):

    def post(self):
        # user_schema = UserSchema()
        # users_schema = UserSchema(many=True)

        if request.is_json:
            email = request.json["email"]
            password = request.json["password"]
        else:
            email = request.form["email"]
            password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            expires = timedelta(minutes=30)
            access_token = create_access_token(identity=email, expires_delta=expires)
            return jsonify(
                message="Login Successful",
                access_token=access_token,
                expires_in=expires.total_seconds(),
            )
        else:
            return jsonify("Bad email or Password"), 401
