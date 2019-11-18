from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt

DB_URI = 'mongodb+srv://becker2203:0SiLKOo6opZm5Tfg@cluster0-fz7se.mongodb.net/app_ranking?retryWrites=true&w=majority'

db = MongoEngine()
app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)
app.config["MONGODB_HOST"] = DB_URI
db.init_app(app)

from app.routes import test_router
from app.routes import auth_router

app.register_blueprint(test_router.test_bp, url_prefix='/api/test')
app.register_blueprint(auth_router.auth_bp, url_prefix='/api/auth')