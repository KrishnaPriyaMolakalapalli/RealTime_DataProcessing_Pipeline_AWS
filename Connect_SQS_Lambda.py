import boto3

lambda_client = boto3.client('lambda')
sqs_client = boto3.client('sqs')

# Add SQS as a trigger to the Lambda function
try:
    response = lambda_client.create_event_source_mapping(
        EventSourceArn="arn:aws:sqs:us-east-2:024848463817:EcommerceTransactionQueue",
        FunctionName='ProcessTransactionFunction',
        Enabled=True,
        BatchSize=10,
        MaximumBatchingWindowInSeconds=10
    )
    print(f"SQS trigger added to Lambda function: {response['UUID']}")
except Exception as e:
    print(f"Error adding SQS trigger to Lambda: {e}")


