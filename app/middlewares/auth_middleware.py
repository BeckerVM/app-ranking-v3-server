from functools import wraps
from flask import request
from app.services.auth_services import decode_token
from jwt import InvalidTokenError

def auth(callback):
  @wraps(callback)
  def wrapper(*args, **kwargs):
    #token = request.headers.get('Authorization').split(' ')[1]
    #print(token)
    if request.headers.get('Authorization') == '':
      return {
        'message': 'No token, autorizacion denegada'
      }, 401
    else:
      token = request.headers.get('Authorization').split(' ')[1]
      try:
        decoded = decode_token(token)
        request.user = decoded
      except InvalidTokenError:
        return {
          'message': 'Token no valido'
        }, 401
   
    return callback(*args, **kwargs)
  
  return wrapper