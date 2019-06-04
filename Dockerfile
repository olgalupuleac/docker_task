FROM ubuntu

MAINTAINER olgalupuleac_sashaorlova

RUN apt-get install python3

RUN pip install localstack

RUN localstack start

RUN export SERVICES=sqs

ADD receive.py receive.py

ADD send.py send.py

ENTRYPOINT ???

CMD ???

ENTRYPOINT usr/bin/mongod