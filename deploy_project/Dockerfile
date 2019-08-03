FROM python:3.6.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-dev gcc libc-dev
RUN aptitude update
RUN aptitude install linux-headers-`uname -r`

WORKDIR /usr/src/app/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT /usr/src/app/entrypoint.sh