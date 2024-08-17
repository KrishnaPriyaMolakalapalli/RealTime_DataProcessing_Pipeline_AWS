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
        ActionsEnabled=True,
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


# Lambda Throttle Alarm
try:
    cloudwatch_client.put_metric_alarm(
        AlarmName='LambdaThrottleAlarm',
        MetricName='Throttles',
        Namespace='AWS/Lambda',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=1,
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=["arn:aws:sns:us-east-2:024848463817:TransactionNotifications"],
        AlarmDescription='Alarm when the Lambda function is throttled',
        Dimensions=[
            {
                'Name': 'FunctionName',
                'Value': 'ProcessTransactionFunction'
            }
        ]
    )
    print("Lambda Throttle Alarm created successfully.")
except Exception as e:
    print(f"Error creating CloudWatch alarm: {e}")

# DynamoDB Read Capacity Alarm
try:
    cloudwatch_client.put_metric_alarm(
        AlarmName='DynamoDBReadCapacityAlarm',
        MetricName='ConsumedReadCapacityUnits',
        Namespace='AWS/DynamoDB',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=100,  
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=["arn:aws:sns:us-east-2:024848463817:TransactionNotifications"],
        AlarmDescription='Alarm when DynamoDB read capacity exceeds threshold',
        Dimensions=[
            {
                'Name': 'TableName',
                'Value': 'Transactions'
            }
        ]
    )
    print("DynamoDB Read Capacity Alarm created successfully.")
except Exception as e:
    print(f"Error creating CloudWatch alarm: {e}")

# DynamoDB Write Capacity Alarm
try:
    cloudwatch_client.put_metric_alarm(
        AlarmName='DynamoDBWriteCapacityAlarm',
        MetricName='ConsumedWriteCapacityUnits',
        Namespace='AWS/DynamoDB',
        Statistic='Sum',
        Period=300,
        EvaluationPeriods=1,
        Threshold=100,  
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=["arn:aws:sns:us-east-2:024848463817:TransactionNotifications"],
        AlarmDescription='Alarm when DynamoDB write capacity exceeds threshold',
        Dimensions=[
            {
                'Name': 'TableName',
                'Value': 'Transactions'
            }
        ]
    )
    print("DynamoDB Write Capacity Alarm created successfully.")
except Exception as e:
    print(f"Error creating CloudWatch alarm: {e}")


# SQS Approximate Number of Messages Alarm
try:
    cloudwatch_client.put_metric_alarm(
        AlarmName='SQSApproximateNumberOfMessagesAlarm',
        MetricName='ApproximateNumberOfMessagesVisible',
        Namespace='AWS/SQS',
        Statistic='Average',
        Period=300,
        EvaluationPeriods=1,
        Threshold=10,  # Adjust based on acceptable message queue size
        ComparisonOperator='GreaterThanOrEqualToThreshold',
        AlarmActions=["arn:aws:sns:us-east-2:024848463817:TransactionNotifications"],
        AlarmDescription='Alarm when there are too many messages in the SQS queue',
        Dimensions=[
            {
                'Name': 'QueueName',
                'Value': 'EcommerceTransactionQueue'
            }
        ]
    )
    print("SQS Approximate Number of Messages Alarm created successfully.")
except Exception as e:
    print(f"Error creating CloudWatch alarm: {e}")





