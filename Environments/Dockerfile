FROM python:3.7
LABEL AUTHOR='Lucas Biason'
LABEL version="1.0"

# Tudo o que for rodado, eh uma stream direto na console, um dockerlogs terá a pilha de erros
ENV PYTHONUNBUFFEDRED  1    

COPY ./requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y postgresql-client
RUN apt-get install -y \
       gcc libc-dev libpq-dev python-dev
RUN apt-get install -y libjpeg-dev zlib1g-dev
RUN pip install -r requirements.txt
#RUN rm -rf /var/lib/apt/lists/*

# Entra direto no /app
WORKDIR /app 
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Executar um container no root pode ser perigoso, 
# seja por conta de alguém conseguir executar um arquivo malicioso ou 
# devido a erros, um processo pode ter consequências inesperadas no tempo de execução.
RUN useradd -m -s /bin/bash -G sudo  user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user


#  Variavel de Env -->
#DATABASE_URL=postgres://${USER_ARG}:${PASS_ARG}@${HOST_ARG}:5432/${DBNAME_ARG}
