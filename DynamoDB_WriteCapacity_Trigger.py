import boto3
import time

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Replace with your DynamoDB table name
table_name = 'Transactions'
table = dynamodb.Table(table_name)

# Function to intentionally trigger DynamoDB write capacity alarm
def trigger_write_capacity_alarm():
    transaction_id_prefix = "test_trigger"
    product_name = "DemoProduct"
    quantity = 1
    unit_price = 10

    print("Starting to trigger DynamoDB write capacity alarm...")

    for i in range(100):  # Adjust the range to control how many writes are performed
        transaction_id = f"{transaction_id_prefix}_{i}"
        try:
            table.put_item(
                Item={
                    'TransactionID': transaction_id,
                    'ProductName': product_name,
                    'Quantity': quantity,
                    'UnitPrice': unit_price,
                    'Status': 'test'
                }
            )
            print(f"Written item {i+1} to DynamoDB.")
        except Exception as e:
            print(f"Error writing to DynamoDB: {e}")
        time.sleep(0.1)  # Adding a slight delay to better demonstrate gradual consumption

    print("Completed writes to DynamoDB. Check your CloudWatch alarms.")

# Run the function to trigger the alarm
trigger_write_capacity_alarm()
