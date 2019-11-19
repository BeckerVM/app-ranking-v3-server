from app import bcrypt
from mongoengine import DoesNotExist
from app.models.user_model import Users as User
from app.validators.register_validators import validate_register_data
from app.validators.login_validators import validate_login_data
from app.services.auth_services import generate_token


def register_user(data):
  errors = validate_register_data(data)
  json = {}

  if errors is not None:
    json = errors, 400
  else:
    email = data['email']
    try:
      user = User.objects.get(email=email)

      json = {
        'error': ['Ya existe el usuario']
      }, 400
    except DoesNotExist:
      hash_password = bcrypt.generate_password_hash(data['password'])
      names = data['names']
      surnames = data['surnames']
      rol = data['rol']

      new_user = User(names=names, password=hash_password, email=email, rol=rol, surnames=surnames)
      new_user.save()

      json = {
        'message': ['Usuario registrado correctamente.']
      }

  return json

def login_user(data):
  errors = validate_login_data(data)
  json = {}

  if errors is not None:
    json = errors, 400
  else:
    email = data['email']
    password = data['password']
    try:
      user = User.objects.get(email=email)

      if bcrypt.check_password_hash(user.password, password):
        token = generate_token({ 'id': str(user.id), 'names': user.names, 'rol': user.rol })

        json = {
          'message': ['Usuario logueado correctamente'],
          'token': token
        }, 200
      else:
        json = {
          'error': ['Usuario o contraseña incorrecta']
        }, 400
    except DoesNotExist:
      json = {
        'error': ['Usuario no existente']
      }, 400

  return json
