FROM python:3.8
COPY . /soundrts
WORKDIR /soundrts
EXPOSE 2500/tcp
EXPOSE 2500/udp
CMD python server.py