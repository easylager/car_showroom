FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY Pipfile* /code/

RUN pip install pipenv && pipenv install --deploy --system

COPY . /code/

CMD ./entrypoint.sh