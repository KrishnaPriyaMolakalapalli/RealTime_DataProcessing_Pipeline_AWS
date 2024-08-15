import boto3

# Initialize CloudWatch client
cloudwatch_client = boto3.client('cloudwatch')

# Create CloudWatch alarm for Lambda errors
try:
    cloudwatch_client.put_metric_alarm(
        AlarmName='LambdaErrorAlarm',
        MetricName='Errors',
        Namespace='AWS/Lambda',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=1,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=["arn:aws:sns:us-east-2:024848463817:TransactionNotifications"],  # Use the SNS topic to send an alarm notification
        AlarmDescription='Alarm when the Lambda function has errors',
        Dimensions=[
            {
                'Name': 'FunctionName',
                'Value': 'ProcessTransactionFunction'
            }
        ]
    )
    print("CloudWatch Alarm for Lambda errors created successfully.")
except Exception as e:
    print(f"Error creating CloudWatch alarm: {e}")




