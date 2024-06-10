FROM python:3.9
WORKDIR /server

ADD server.py /server/

CMD [ "python", "./server.py" ]

EXPOSE 8000