# serverless-flask-model

## Setup

### AWS Credentials
If you are using AWS environment you'll need to setup the credentials. 

This following link will help you with this step:
[AWS Credentials](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html)

### Install NPM
```
sudo apt install npm
```
### Install Serverless
```
sudo npm install -g serverless
```
### Start Serverless Project
Run the command: **``` serverless ```** on the project folder and follow the serverless steps on terminal.

### Serverless plugins
```
sls plugin install -n serverless-wsgi
sls plugin install -n serverless-python-requirements
```

### Setup DynamoDB
Run the python scripts to create and populate an example table in DynamoDB. 
```
python3 scripts/create_tables.py
python3 scripts/entering_data.py
```
After the tables creation, update the environment file in resource folder with the table ARN.

## Deploy

### DEV
```
sls deploy --stage dev
```
### PROD
```
sls deploy --stage dev
```
