FROM python:3.8-slim-buster

LABEL maintainer="Jk"

WORKDIR /python-docker

COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_APP="app" \
  FLASK_RUN_PORT=1234

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]