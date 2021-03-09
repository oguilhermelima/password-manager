import boto3
from boto3.dynamodb.conditions import Key


_DYNAMODB = boto3.resource('dynamodb')
_TABLE = _DYNAMODB.Table('Passwords')


def get_passwords_by_user_id(user_id):
    response = _TABLE.scan(FilterExpression=Key('user_id').eq(user_id))
    result = response['Items']
    while 'LastEvaluatedKey' in response:
        response = _TABLE.scan(ExclusiveStartKey=response['LastEvaluatedKey'], FilterExpression=Key('user_id').eq(user_id))
        result.extend(response['Items'])
    return result
