from flask import Blueprint, request
from app.controllers.auth_controller import register_user as register, login_user as login
from app.middlewares.auth_middleware import auth


auth_bp = Blueprint('auth_bp', __name__)

# Ruta api/auth/register - POST
@auth_bp.route('/register', methods=['POST'])
def register_user():
  json = register(request.json)
  return json


@auth_bp.route('/protected', methods=['GET'])
@auth
def protected():
  print(request.user)
  return {
    'user': request.user
  }

# Ruta api/auth/login/<type_user> - POST
@auth_bp.route('/login/<type_user>', methods=['POST'])
def login_user(type_user):
  print(type_user)
  json = login(request.json)
  return json