FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD python manage.py collectstatic --no-input && python manage.py makemigrations --no-input && python manage.py migrate --no-input && python manage.py runserver 0.0.0.0:8000