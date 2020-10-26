import boto3
from boto3.dynamodb.conditions import Key


_DYNAMODB = boto3.resource('dynamodb')
_TABLE = _DYNAMODB.Table('Passwords')


def create_password(password):
    _TABLE.put_item(Item=password)


def get_passwords(user_id):
    response = _TABLE.scan(FilterExpression=Key('user_id').eq(user_id))
    result = response['Items']
    while 'LastEvaluatedKey' in response:
        response = _TABLE.scan(ExclusiveStartKey=response['LastEvaluatedKey'], FilterExpression=Key('user_id').eq(user_id))
        result.extend(response['Items'])
    return result


def get_password(user_id, password_id):
    return _TABLE.query(KeyConditionExpression=Key('user_id').eq(user_id) & Key("id").eq(password_id))['Items']
