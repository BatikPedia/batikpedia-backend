FROM python:3.9
LABEL maintainer="darielgaz@gmail.com"

WORKDIR /

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN 

CMD python manage.py makemigrations && python manage.py migrate && gunicorn batikpedia.wsgi:application --bind 0.0.0.0:8080