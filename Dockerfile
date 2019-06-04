FROM ubuntu

MAINTAINER olgalupuleac_sashaorlova

RUN apt-get update &&  apt-get install -y python3.6

RUN apt-get update &&  apt-get install -y python3-pip && pip3 install localstack

RUN export SERVICES=sqs

ADD receive.py receive.py

ADD send.py send.py

RUN python3 send.py

ENTRYPOINT python3

CMD ["receive.py", "A", "B"]