FROM python:3.11

RUN mkdir code
WORKDIR code

ADD . /code/
ADD .env.docker /code/.env

RUN pip install -r requirements.txt

CMD gunicorn base.wsgi:application -b 0.0.0.0:8000 && python manage.py migrate && python manage.py csu && python manage.py loaddata fixtures/groups.json && python manage.py runserver 0.0.0.0:8000

