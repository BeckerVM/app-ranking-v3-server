from functools import wraps
from flask import request

def auth(callback):
  @wraps(callback)
  def wrapper(*args, **kwargs):
    authenticated = False
    print(request.headers.get('Authorization'))
    if authenticated:
      return { 'success': False }
    else:
      return callback(*args, **kwargs)
  
  return wrapper