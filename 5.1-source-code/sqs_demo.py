#!/usr/bin/env python
import time
import os
import sys
import boto3

SQS_QUEUE_URL = ''

def listen_sqs():
    while True:
        sqs = boto3.client('sqs')
        response = sqs.receive_message(QueueUrl=SQS_QUEUE_URL,
                                       MaxNumberOfMessages=1,
                                       MessageAttributeNames=['All'],
                                       VisibilityTimeout=1,
                                       WaitTimeSeconds=0)
        if 'Messages' in response:
            message = response['Messages'][0]
            body = message['Body']
            print("Message received: \n\n{0}\n".format(message))
            sqs.delete_message(
                QueueUrl=SQS_QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle']
            )
            print('Message deleted!')
        sys.stdout.flush()
        time.sleep(10)


if __name__ == "__main__":
    listen_sqs()
