ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system -d

COPY . ./

EXPOSE 8000

ENTRYPOINT ["./start.sh"]