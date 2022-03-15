FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY Pipfile* /code/

RUN pip install pipenv
RUN pipenv install --system --ignore-pipfile
COPY ./entrypoint.sh .
COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

COPY . /code/

ENTRYPOINT ["./entrypoint.sh"]