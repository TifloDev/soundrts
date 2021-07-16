FROM python:3.8
RUN mkdir -p /soundrts
WORKDIR /soundrts
COPY . /soundrts
RUN python -m pip install -Ur /usr/src/soundrts/requirements.txt
EXPOSE 2500/tcp
EXPOSE 2500/udp
CMD python server.py