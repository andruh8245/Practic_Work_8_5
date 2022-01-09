FROM python:latest

WORKDIR /rfam

COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY rfam.py .
COPY conf/rfam.conf .