FROM python:3.9
WORKDIR /server

COPY ./server.py /server

CMD [ "python", "./server.py" ]

EXPOSE 8000:8000