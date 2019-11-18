from marshmallow import fields, Schema, validates, ValidationError

class RegisterSchema(Schema):
  names = fields.String(required=True, error_messages={ 'required': 'Sus nombres son obligatorios.' })
  password = fields.String(required=True, error_messages={ 'required': 'Su contraseña es obligatoria.' })
  email = fields.Email(required=True, error_messages={ 'required': 'Su correo electronico es obligatorio' })
  surnames = fields.String(required=True, error_messages={ 'required': 'Sus apellidos son obligatorios' })
  rol = fields.String(required=True, error_messages={ 'required': 'Su rol es obligatorio' })


def validate_register_data(data):
  try:
    RegisterSchema().load(data)
  except ValidationError as err:
    return err.messages