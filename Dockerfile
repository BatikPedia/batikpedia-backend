FROM python:3.9-alpine
LABEL maintainer="darielgaz@gmail.com"

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

VOLUME /mnt/secrets

RUN cp /mnt/secrets/CLOUD_RUN_SERVICE_ACCOUNT ~/.gcp/service-account.json

CMD ["gunicorn", "batikpedia.wsgi:application", "--bind", "0.0.0.0:8000"]