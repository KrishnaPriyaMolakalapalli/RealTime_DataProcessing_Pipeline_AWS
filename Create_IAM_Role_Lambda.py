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

# Define the policy document with limited permissions
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                # SQS permissions
                "sqs:ReceiveMessage",
                "sqs:DeleteMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "arn:aws:sqs:us-east-2:024848463817:EcommerceTransactionQueue"
        },
        {
            "Effect": "Allow",
            "Action": [
                # Lambda permissions to be invoked by SQS
                "lambda:InvokeFunction"
            ],
            "Resource": "arn:aws:lambda:us-east-2:024848463817:function:ProcessTransactionFunction"
        },
        {
            "Effect": "Allow",
            "Action": [
                # SNS permissions to publish messages
                "sns:Publish"
            ],
            "Resource": [
                "arn:aws:sns:us-east-2:024848463817:TransactionNotifications",
                "arn:aws:sns:us-east-2:024848463817:OrderRequestNotifications"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                # DynamoDB permissions for the Lambda function to write to the table
                "dynamodb:PutItem",
                "dynamodb:UpdateItem"
            ],
            "Resource": "arn:aws:dynamodb:us-east-2:024848463817:table/Transactions"
        },
        {
            "Effect": "Allow",
            "Action": [
                # CloudWatch logs 
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }, 
        {
          "Effect": "Allow",
          "Action": [
              # CloudWatch Alarms
              "cloudwatch:PutMetricData",
              "cloudwatch:PutMetricAlarm",
              "cloudwatch:DeleteAlarms",
              "cloudwatch:DescribeAlarms"
          ]
          "Resource": "*"
        }

    ]
}


# Attach the custom policy to the role
iam_client.put_role_policy(
    RoleName=role_name,
    PolicyName="EcommerceTransactionPolicy",
    PolicyDocument=json.dumps(policy_document)
)
print(f"Policy 'EcommerceTransactionPolicy' attached to role '{role_name}' successfully.")

