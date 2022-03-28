FROM python:3.8.3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r requirements.txt
COPY . /code/