FROM python:3.9-alpine
LABEL maintainer="darielgaz@gmail.com"

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "batikpedia.wsgi:application", "--bind", "0.0.0.0:8080"]