FROM python:3.6.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-dev gcc linux-headers libc-dev

WORKDIR /usr/src/app/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT /usr/src/app/entrypoint.sh