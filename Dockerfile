FROM python:3.9
WORKDIR /server

EXPOSE 8000

CMD [ "python", "./server.py" ]