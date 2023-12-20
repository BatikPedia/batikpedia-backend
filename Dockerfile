FROM python:3.9-alpine
LABEL maintainer="darielgaz@gmail.com"

WORKDIR /

COPY requirements.txt ./requirements.txt
RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install -r requirements.txt

COPY . .

RUN 

CMD python manage.py makemigrations && python manage.py migrate && gunicorn batikpedia.wsgi:application --bind 0.0.0.0:8080