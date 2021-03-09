from src.infrastructure.password import database
import uuid
from datetime import datetime


def create_password(password):
    password['id'] = str(uuid.uuid4())
    password['created_at'] = str(datetime.now())
    database.create_password(password)
    return password


def get_passwords(user_id):
    return database.get_passwords(user_id)


def get_password(user_id, password_id):
    return database.get_password(user_id, password_id)
