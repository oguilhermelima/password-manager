import boto3

_DYNAMODB = boto3.resource('dynamodb')
_TABLE = _DYNAMODB.Table('Passwords')


def create_password_db(password):
    _TABLE.put_item(Item=password)

