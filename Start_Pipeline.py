import boto3
import json

sqs_client = boto3.client('sqs')

# Define the transactions to send to the queue
transactions = [
    {"transaction_id": "1001", "product_name": "Laptop", "quantity": 1, "unit_price": 1000},
    {"transaction_id": "1002", "product_name": "Monitor", "quantity": 2, "unit_price": 200},
    {"transaction_id": "1003", "product_name": "Mouse", "quantity": 10, "unit_price": 20},
    {"transaction_id": "1004", "product_name": "Keyboard", "quantity": 0, "unit_price": 50},   
    {"transaction_id": "1005", "product_name": "Desk", "quantity": 150, "unit_price": 300},  # Large order: quantity > 100
    {"transaction_id": "1006", "product_name": "Chair", "quantity": -1, "unit_price": 150}   
]

for transaction in transactions:
    try:
        sqs_client.send_message(
            QueueUrl="https://sqs.us-east-2.amazonaws.com/024848463817/EcommerceTransactionQueue",
            MessageBody=json.dumps(transaction)
        )
        print(f"Transaction {transaction['transaction_id']} sent to SQS successfully.")
    except Exception as e:
        print(f"Error sending transaction {transaction['transaction_id']} to SQS: {e}")








