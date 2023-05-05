# syntax=docker/dockerfile:1

FROM python:3.10.8

WORKDIR /bot
COPY /requirements.txt /bot ./

RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["sh", "-c", "python3 /bot/main.py"]
