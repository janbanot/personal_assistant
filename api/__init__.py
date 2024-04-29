import os
import sys
import logging
from flask import Flask
from api.extensions import db, ma, jwt
from api.routes.login_view import LoginView
from api.routes.chat_view import ChatView
from api.routes.clear_context_view import ClearView
from api.routes.test_view import TestView
from api.routes.yt_summary_view import YTSummaryView
from api.routes.check_english_view import CheckEnglishView


def create_app():
    app = Flask(__name__)
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "this is a secret key")
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("POSTGRES_URL", "")

    # Initialize the instances with the app
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    app.add_url_rule('/', view_func=TestView.as_view('test_view'), methods=['GET',])
    app.add_url_rule('/login', view_func=LoginView.as_view('login_view'), methods=['POST',])
    app.add_url_rule('/chat', view_func=ChatView.as_view('chat_view'), methods=['POST',])
    app.add_url_rule('/clear-context', ClearView.as_view('clear_view'), methods=['POST',])
    app.add_url_rule('/yt-summary', view_func=YTSummaryView.as_view('yt_summary'), methods=['POST',])
    app.add_url_rule('/check-english', view_func=CheckEnglishView.as_view('check_english_route'), methods=['POST',])

    # Configure logging
    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])
    app.logger.info("Starting application")

    return app
