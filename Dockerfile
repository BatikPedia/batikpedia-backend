FROM python:3.9-alpine
LABEL maintainer="darielgaz@gmail.com"

COPY ./requirements.txt /requirements.txt
COPY ./ /app

WORKDIR /app

# Create virtual environtment called /py
# Install dependencies in virtual environment /py
# Run add user to prevent full root access, for security purposes.
RUN python -m venv /py && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

# Switch to non-root user in Docker.
USER django-user

CMD [ "uvicorn", "batikpedia.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level=debug" ]