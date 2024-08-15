import boto3

# Initialize SNS client
sns_client = boto3.client('sns')

# Replace with your actual SNS topic ARN and email address
topic_arn = 'arn:aws:sns:us-east-2:024848463817:TransactionNotifications'
email_address = 'krishnapriyamolakalapalli3@gmail.com'

# Subscribe the email address to the SNS topic
try:
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email_address,
        ReturnSubscriptionArn=True
    )
    subscription_arn = response['SubscriptionArn']
    print(f"Subscription created successfully. Subscription ARN: {subscription_arn}")
    print(f"Please check your email ({email_address}) to confirm the subscription.")
except Exception as e:
    print(f"Error creating SNS subscription: {e}")
