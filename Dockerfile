FROM ubuntu:18.10

MAINTAINER Andrew St Pierre "asaintp97@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python3 python3-dev python3-pip nginx
RUN pip3 install uwsgi boto3 flask wtforms flask-wtf

COPY . /app
COPY ./nginx.conf /etc/nginx/sites-enabled/default
WORKDIR ./app

CMD service nginx start && uwsgi -s /tmp/uwsgi.sock --chmod-socket=666 --manage-script-name --mount /=app:app
