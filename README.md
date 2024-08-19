# RealTime_DataProcessing_Pipeline_AWS
Real time data processing pipeline that processes the ecommerce transactions and store in DynamoDB


Objective: To design and build a real time data processing pipeline using AWS SQS, Lambda, DynamoDB, and SNS. Monitor the pipeline using CloudWatch with alarms for proactive alerting.

Tech Stack:

1. SQS for Data Ingestion: Queue incoming transactions to manage load.
2. Lambda for Processing: Automatically validate and process each transaction.
3. DynamoDB for Storage: Scalable and reliable storage for transaction data.
4. SNS for Notifications: Automated alerts for critical events
5. CloudWatch for Monitoring: Proactive monitoring with alarms to ensure efficient operations.


Steps:
1.	Data Ingestion: Use SQS to queue incoming transaction data from an e-commerce platform.
2.	Notification: Use SNS to send notifications for certain transaction events (e.g., large orders).
3.	Processing: Implement a Lambda function to process the transactions from SQS, validate the data, and store valid transactions in DynamoDB.
4.	Monitoring: Use CloudWatch to monitor Lambda execution and DynamoDB performance.


Repository Structure:

1. Create_SQS_Queue.py : Creates a queue in SQS
2. Create_SNS_Topic.py, Create_OrderRequest_SNS.py : Creates SNS Topics
3. Subscribe_SNS_Topic.py, Subscribe_SNS_OrderRequest.py : Subscribes to SNS topics
4. Create_DynamoDB_Table.py : Creates table in DynamoDB
5. Create_IAM_Role_Lambda.py : Creates IAM role for Lambda to access SQS, SNS, DynamoDB, perform basic Lambda operations
6. lambda_function.py : Lambda Function Script
7. Create_Lambda_Function.py : Creates Lambda function 
8. Connect_SQS_Lambda.py : Connect Lambda to SQS Queue
9. Cloud_Watch.py : Creates cloud watch alarms
10. Start_Pipeline.py : Starts pipeline by sending messages to queue
11. DynamoDB_WriteCapacity_Trigger.py : Code to trigger DynamoDB write capacity

Conclusion - The Realtime data processing pipeline built using ASW services like SQS, Lambda, SNS, DynamoDB, CloudWatch ensures instantaneous processing of data, provides validation and stores in a reliable location. This pipeline also monitors and alerts technical teams about certain events to improve and maintain operational efficiency and customer satisfaction


Contributers -

Nandini Javvaji:
   1. SQS Queue and SNS Topics Creation: Created an SQS Queue and SNS topics, Then subscribed to SNS topics. Scripts - Create_SQS_Queue.py, Create_SNS_Topic.py, Create_OrderRequest_SNS.py, Subscribe_SNS_Topic.py, Subscribe_SNS_OrderRequest.py
   2. IAM Role Creation: Created an IAM role with the necessary permissions for the Lambda. Scripts - Create_IAM_Role_Lambda.py

Krishna Priya Molakalapalli: 
  1. Lambda Function Creation: Wrote data processing script for lambda function and created a lambda function. Scripts - lambda_function.py, Create_Lambda_Function.py
  2. Cloud watch alarms creation: Created Cloud watch alarms and wrote a script to trigger alarm for demo. Scripts -  Cloud_Watch.py, DynamoDB_WriteCapacity_Trigger.py

Kaveri Reddy Veluri: 
  1. DynamoDB Table Creation: Created a table in DynamoDB. Script - Create_DynamoDB_Table.py
  2. Connect SQS and Lambda, Send messages to Queue. Scripts - Connect_SQS_Lambda.py, Start_Pipeline.py
  3. Pushing to GitHub: Pushed all the code, scripts, and configuration files to the GitHub repository.

Together Work: The presentation (PPT) preparation was a collaborative effort by Krishna Priya, Nandini, and Kaveri. Together, we had designed the slides, explained the architecture, and included relevant diagrams, screenshots, and explanations for each component of the pipeline.
