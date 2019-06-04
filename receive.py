#!/usr/bin/env python3
import boto3
import sys
# Create SQS client
sqs = boto3.resource('sqs', endpoint_url='http://localhost:4576/')

name1, name2 = sys.argv[1], sys.argv[2]
queue1 = sqs.get_queue_by_name(QueueName=name1)
queue2 = sqs.get_queue_by_name(QueueName=name2)

while True:
    for message in queue1.receive_messages():
        n = message.body
        print(n)
        queue2.send_message(MessageBody=str(int(n) + 1))
        message.delete()

