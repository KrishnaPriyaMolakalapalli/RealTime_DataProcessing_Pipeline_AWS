import boto3

# Initialize Lambda client
lambda_client = boto3.client('lambda')


# Read the zipped Lambda function code
with open('lambda_function.zip', 'rb') as f:
    zipped_code = f.read()

# Create the Lambda function
try:
    response = lambda_client.create_function(
        FunctionName='ProcessTransactionFunction',
        Runtime='python3.8',
        Role='arn:aws:iam::024848463817:role/LambdaSQSDynamoDBRole', 
        Handler='lambda_function.lambda_handler',
        Code={
            'ZipFile': zipped_code
        },
        Environment={
            'Variables': {
                'DYNAMODB_TABLE': 'Transactions',
                'SNS_TOPIC_ARN': 'arn:aws:sns:us-east-2:024848463817:TransactionNotifications',
                'INVENTORY_NOTIFICATION_TOPIC_ARN': 'arn:aws:sns:us-east-2:024848463817:OrderRequestNotifications'
            }
        },
        Timeout=10,
        MemorySize=128
    )
    print(f"Lambda function created: {response['FunctionArn']}")
except Exception as e:
    print(f"Error creating Lambda function: {e}")
