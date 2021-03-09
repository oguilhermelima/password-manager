from src.domain.password.get_passwords import get_passwords
from src.domain.password.create_password import create_password
from src.domain.password.get_password import get_password


def get_passwords_controller(event, context):
    user_id = event['headers']['user_id']
    passwords = get_passwords(user_id)
    return passwords, 200


def create_password_controller(event, context):
    data = event['body']
    response = create_password(data)
    return response, 201


def get_password_controller(event, context):
    user_id = event['headers']['user_id']
    password_id = event['pathParameters']['password_id']
    password = get_password(user_id, password_id)
    return password, 200
