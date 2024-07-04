FROM python:3.11

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip


COPY README.md /code/

RUN pip install -r requirements.txt

COPT . .