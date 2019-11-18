from flask import Blueprint, jsonify

test_bp = Blueprint('test_bp', __name__)

# Ruta api/test/test - GET
@test_bp.route('/test')
def test():
  return jsonify({
    'status': 200
  })