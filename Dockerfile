FROM python:3.7

MAINTAINER olgalupuleac_sashaorlova

RUN apt-get update &&  apt-get install -y python3-pip && pip3 install boto3

RUN export SERVICES=sqs

ADD receive.py receive.py

ADD send.py send.py
