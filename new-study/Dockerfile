# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /code
COPY requirements.txt requirements.txt
COPY init init

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x init/entrypoint.sh
ENTRYPOINT [ "sh", "init/entrypoint.sh" ]
