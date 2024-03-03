import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

load_dotenv()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if (request.method == 'GET'):
        data = "hello world"
        app.logger.info('Request: %s', request)
        app.logger.info('Response: %s', data)
        return jsonify({'data': data})


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG_MODE', 'False')
    app.run(debug=debug_mode.lower() == 'true')
