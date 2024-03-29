import os
import sys
import logging
from dotenv import load_dotenv
from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import check_password_hash
from api.conversation import chat, clear

load_dotenv()
app = Flask(__name__)
SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "this is a secret key")
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL", "")

db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])
app.logger.info("Starting application")


@app.route("/", methods=["GET"])
@jwt_required()
def home_route():
    if request.method == "GET":
        data = "hello world"
        app.logger.info("Request: %s", request)
        app.logger.info("Response: %s", data)
        return jsonify({"data": data})


@app.route("/login", methods=["POST"])
def login_route():
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


app.register_blueprint(chat)
app.register_blueprint(clear)


# TODO: fix type and move to a separate file
class User(db.Model):  # type: ignore
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    login = Column(String, unique=True)
    password_hash = Column(String)


# TODO: move to a separate file
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "email", "login", "password_hash")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


if __name__ == "__main__":
    is_debug = os.getenv("FLASK_DEBUG_MODE", "False").lower() == "true"
    app.run(debug=is_debug)
