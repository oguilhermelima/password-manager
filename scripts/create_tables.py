import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='Passwords',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'user_id',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
