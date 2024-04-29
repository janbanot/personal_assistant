import os
from dotenv import load_dotenv
from api import create_app

load_dotenv()
app = create_app()

if __name__ == "__main__":
    is_debug = os.getenv("FLASK_DEBUG_MODE", "False").lower() == "true"
    app.run(debug=is_debug)
