from src.infrastructure.password.create_password import create_password_db
import uuid
from datetime import datetime


def create_password(password):
    password['id'] = str(uuid.uuid4())
    password['created_at'] = str(datetime.now())
    create_password_db(password)
    return password
