from jwt import encode, decode
from app import SECRET_KEY

def generate_token(payload):#{ 'id':, 'names':, rol: '' }
  token = encode(payload, SECRET_KEY, algorithm='HS256')
  return token.decode('utf-8')

def decode_token(token):
  return decode(token, SECRET_KEY, algorithms='HS256')