from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from src.routes import test_router

app.register_blueprint(test_router.test_bp, url_prefix='/api/test')