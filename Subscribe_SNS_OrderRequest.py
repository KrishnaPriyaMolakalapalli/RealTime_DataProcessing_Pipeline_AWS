import boto3

# Initialize SNS client
sns_client = boto3.client('sns')

# Replace with your actual SNS topic ARN and inventory team's email address
topic_arn = 'arn:aws:sns:us-east-2:024848463817:OrderRequestNotifications'
inventory_team_email = 'krishnapriyamolakalapalli3@gmail.com'

# Subscribe the inventory team to the SNS topic
try:
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=inventory_team_email,
        ReturnSubscriptionArn=True
    )
    subscription_arn = response['SubscriptionArn']
    print(f"Subscription created successfully. Subscription ARN: {subscription_arn}")
    print(f"Please check the inventory team email ({inventory_team_email}) to confirm the subscription.")
except Exception as e:
    print(f"Error creating SNS subscription: {e}")
