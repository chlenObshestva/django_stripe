FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app/

RUN pip install --upgrade pip
COPY ./requirements.txt  .
RUN pip install -r requirements.txt

COPY / /app/

CMD ["python", "manage.py", "migrate"]
ENTRYPOINT ["python", "manage.py", "runserver"]