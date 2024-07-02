FROM ubuntu:22.04 

WORKDIR /worksapce

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt

ADD ./app /worksapce/app

CMD [ "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8080" ]
