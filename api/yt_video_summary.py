from dotenv import load_dotenv
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

load_dotenv()

yt_summary = Blueprint('yt_summary', __name__)


@yt_summary.route('/yt-summary', methods=['POST'])
@jwt_required()
def yt_summary_route():
    data = request.get_json()
    return jsonify({"message": data})
