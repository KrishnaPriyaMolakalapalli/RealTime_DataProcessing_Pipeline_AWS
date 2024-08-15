import boto3

# Initialize SNS client
sns_client = boto3.client('sns')

# Create SNS Topic for order request notifications
topic_name = "OrderRequestNotifications"
try:
    response = sns_client.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print(f"SNS Topic {topic_name} created successfully. ARN: {topic_arn}")
except Exception as e:
    print(f"Error creating SNS topic: {e}")
