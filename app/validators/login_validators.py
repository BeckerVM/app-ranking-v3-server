from marshmallow import fields, Schema, validates, ValidationError

class LoginSchema(Schema):
  email = fields.Email(required=True, error_messages={ 'required': 'Correo electronico requerido.' })
  password = fields.String(required=True, error_messages={ 'required': 'Contraseña requerido.' })

def validate_login_data(data):
  try:
    LoginSchema().load(data)
  except ValidationError as err:
    return err.messages