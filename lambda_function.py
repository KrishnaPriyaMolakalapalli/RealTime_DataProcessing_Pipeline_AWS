import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    sns = boto3.client('sns')
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    
    for record in event['Records']:
        # Get the message from SQS
        message = json.loads(record['body'])
        transaction_id = message['transaction_id']

        # Check if transaction_id is None or invalid
        if not transaction_id:
            print(f"Invalid transaction_id: {transaction_id}. Skipping this record.")
            continue  # Skip processing this record
            
        product_name = message['product_name']
        quantity = message['quantity']
        unit_price = message['unit_price']

        # Initialize the status of the transaction
        status = 'confirmed'

        # Validate quantity
        if quantity <= 0:
            status = 'incomplete'
            print(f"Invalid transaction: {transaction_id}. Quantity must be greater than 0.")
        
        # Send notification for large orders based on quantity
        if quantity > 100:  # Threshold for large orders
            status = 'pending'
            sns.publish(
                TopicArn=os.environ['SNS_TOPIC_ARN'],
                Message=f'Large order received: TransactionID {transaction_id}, Product {product_name}, Quantity {quantity}\nVerify the transaction.',
                Subject='Large Transaction Alert'
            )

        # Store the transaction in DynamoDB with the status
        table.put_item(Item={
            'TransactionID': transaction_id,
            'ProductName': product_name,
            'Quantity': quantity,
            'UnitPrice': unit_price,
            'Status': status
        })           

        if status == 'confirmed':
            inventory_notification_topic_arn = os.environ['INVENTORY_NOTIFICATION_TOPIC_ARN']
            try:
                sns.publish(
                    TopicArn=inventory_notification_topic_arn,
                    Message=(
                        f"Order Request:\n\n"
                        f"Order ID: {transaction_id}\n"
                        f"Product: {product_name}\n"
                        f"Quantity: {quantity}\n"
                        f"Total Price: ${quantity * unit_price}\n\n"
                        f"Please process the order and update the inventory."
                    ),
                    Subject='Order Request Notification'
                )
                print(f"Order request notification sent to inventory team for transaction {transaction_id}.")
            except Exception as e:
                print(f"Failed to send order request notification for transaction {transaction_id}: {e}")
    
   
    return {
        'statusCode': 200,
        'body': json.dumps('Processed message successfully')
    }


