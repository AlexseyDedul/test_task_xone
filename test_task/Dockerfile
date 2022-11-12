FROM python:3.10
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /test_task

COPY ./req.txt ./
RUN pip install --upgrade pip
RUN pip install -r req.txt
COPY . .