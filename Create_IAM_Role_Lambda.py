import boto3
import json

# Initialize IAM client
iam_client = boto3.client('iam')

# Create IAM role for Lambda
role_name = "LambdaSQSDynamoDBRole"
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Create the IAM role
try:
    response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Role for Lambda to access SQS, DynamoDB, and SNS"
    )
    print(f"Role {role_name} created successfully.")
except Exception as e:
    print(f"Error creating role: {e}")
    exit(1)

# Attach necessary policies to the role
# Grant permissions to access SQS, DynamoDB, SNS, and write logs to CloudWatch

policy_arn_list = [
    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",  # Allows Lambda to write to CloudWatch
    "arn:aws:iam::aws:policy/AmazonSQSFullAccess",  # Allows access to SQS
    "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",  # Allows access to DynamoDB
    "arn:aws:iam::aws:policy/AmazonSNSFullAccess"  # Allows access to SNS
]

for policy_arn in policy_arn_list:
    iam_client.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy_arn
    )
    print(f"Attached policy {policy_arn} to role {role_name}.")
