#!/usr/bin/env python3
import boto3

sqs = boto3.resource('sqs', endpoint_url='http://localhost:4576/')
queue1 = sqs.create_queue(QueueName='A')
queue2 = sqs.create_queue(QueueName='B')
queue1.send_message(MessageBody='1')
queue1.send_message(MessageBody='2')

