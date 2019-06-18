#!/usr/bin/env python3
import boto3
import time

time.sleep(10)

sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576', region_name='eu_west_1', aws_access_key_id='ACCESS_KEY', aws_secret_access_key='SECRET_KEY')
queue1 = sqs.create_queue(QueueName='A')
queue2 = sqs.create_queue(QueueName='B')
queue1.send_message(MessageBody='1')

