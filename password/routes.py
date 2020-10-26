from flask import Blueprint, request, jsonify
from password.schema import PasswordSchema
from utils.params_validator import required_params
import password.service as service

password_bp = Blueprint('passwords', __name__)


@password_bp.route("/passwords/")
def get_passwords():
    user_id = request.headers['user_id']
    passwords = service.get_passwords(user_id)
    return jsonify(passwords), 200


@password_bp.route("/passwords/", methods=["POST"])
@required_params(PasswordSchema())
def create_password():
    data = request.get_json()
    response = service.create_password(data)
    return jsonify(response), 201


@password_bp.route("/passwords/<password_id>", methods=["GET"])
def get_password(password_id):
    user_id = request.headers['user_id']
    password = service.get_password(user_id, password_id)
    return jsonify(password), 200
