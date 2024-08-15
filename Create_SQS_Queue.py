import boto3

# Initialize SQS client
sqs_client = boto3.client('sqs')

# Create SQS Queue
queue_name = "EcommerceTransactionQueue"
try:
    response = sqs_client.create_queue(
        QueueName=queue_name,
        Attributes={
            'DelaySeconds': '0',
            'MessageRetentionPeriod': '86400'  # 1 day
        }
    )
    queue_url = response['QueueUrl']
    print(f"SQS Queue {queue_name} created successfully. URL: {queue_url}")
except Exception as e:
    print(f"Error creating SQS queue: {e}")
