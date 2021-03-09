import boto3
from boto3.dynamodb.conditions import Key

_DYNAMODB = boto3.resource('dynamodb')
_TABLE = _DYNAMODB.Table('Passwords')


def get_password_db(user_id, password_id):
    return _TABLE.query(KeyConditionExpression=Key('user_id').eq(user_id) & Key("id").eq(password_id))['Items']
