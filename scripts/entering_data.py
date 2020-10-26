import string
import random
import boto3
import uuid


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Passwords')

user_id = str(uuid.uuid4())
passwords = [
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Facebook", "password": get_random_string(16), "category": None},
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Twitter", "password": get_random_string(16), "category": None},
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Instagram", "password": get_random_string(16), "category": None},
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Google", "password": get_random_string(16), "category": None},
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Outlook", "password": get_random_string(16), "category": None},
    {"user_id": user_id, "id": str(uuid.uuid4()), "name": "Notion", "password": get_random_string(16), "category": None}]

for password in passwords:
    print(password)
    table.put_item(Item=password)



