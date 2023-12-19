FROM python:3.9-alpine
LABEL maintainer="darielgaz@gmail.com"

WORKDIR /

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"