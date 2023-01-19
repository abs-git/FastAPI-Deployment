FROM ubuntu:20.04

WORKDIR /code

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3-pip

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

ADD ./app /code

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]
