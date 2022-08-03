"""To start flask application run this file."""

from app import create_app
from config import load_config

if __name__ == "__main__":
    AppConfig = load_config()
    app = create_app(AppConfig)
    PORT = 5000
    app.run(host="0.0.0.0", port=PORT)
