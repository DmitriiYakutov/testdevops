FROM python:3.9
WORKDIR /server

ADD server.py /server/

RUN pip install psycopg2

CMD [ "python", "./server.py" ]

EXPOSE 8000
EXPOSE 5432