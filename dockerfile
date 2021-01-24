FROM python:3.8
RUN mkdir -p /usr/src/soundrts
WORKDIR /usr/src/soundrts
COPY . /usr/src/soundrts
RUN python -m pip install -Ur /usr/src/soundrts/requirements.txt
EXPOSE 2500/tcp
EXPOSE 2500/udp
CMD python server.py