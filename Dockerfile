FROM python:3.7-alpine
MAINTAINER CodedBuzz

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
ADD requirements.txt ./
WORKDIR /src
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt

COPY ./src /src
EXPOSE 6000

#RUN addUser -D user
#USER user

