import boto3

# Initialize DynamoDB client
dynamodb_client = boto3.client('dynamodb')

# Create DynamoDB Table
table_name = "Transactions"
try:
    response = dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'TransactionID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'TransactionID',
                'AttributeType': 'S'  # String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"DynamoDB Table {table_name} created successfully.")
except Exception as e:
    print(f"Error creating DynamoDB table: {e}")
