#!/usr/bin/env python3
import boto3
import sys
import time

time.sleep(20)
sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576', region_name='eu_west_1',
                     aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY')

name1, name2 = sys.argv[1], sys.argv[2]
queue1 = sqs.get_queue_by_name(QueueName=name1)
queue2 = sqs.get_queue_by_name(QueueName=name2)

while True:
    for message in queue1.receive_messages():
        n = message.body
        print(n, flush=True)
        message.delete()
        queue2.send_message(MessageBody=str(int(n) + 1))

