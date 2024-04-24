FROM python:3.7
LABEL AUTHOR="Lucas Biason"
LABEL version="1.0"

ENV PYTHONUNBUFFEDRED 1

COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y postgresql-client
RUN apt-get install -y \
       gcc libc-dev libpq-dev python-dev
RUN apt-get install libjpeg-dev zlib1g-dev
RUN pip install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN useradd -m -s /bin/bash -G sudo  user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
