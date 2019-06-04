#!/usr/bin/env python3
import boto3

# Create SQS client
sqs = boto3.resource('sqs', endpoint_url='http://localhost:4576/')
queue1 = sqs.get_queue_by_name(QueueName='A')
queue2 = sqs.get_queue_by_name(QueueName='B')

while True:
    for message in queue1.receive_messages():
        n = message.body
        print(n)
        queue2.send_message(MessageBody=str(int(n) + 1))
        message.delete()

