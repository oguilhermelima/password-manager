from src.infrastructure.password.get_password import get_password_db


def get_password(user_id, password_id):
    return get_password_db(user_id, password_id)
