FROM python:3.8-slim-buster

LABEL "maintainer"="puppyco corporarted"

WORKDIR /python-docker

RUN pip3 install Flask

COPY . .

ENV FLASK_APP="dogworld" \
  FLASK_RUN_PORT=1234

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]