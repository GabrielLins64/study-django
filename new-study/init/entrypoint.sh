#!/bin/bash

until python /code/manage.py makemigrations; do
  echo "O banco de dados ainda não está disponível. Tentando novamente em 3 segundos."
  sleep 3
done

python /code/manage.py migrate && \
sh /code/init/load_mocks.sh && \
python /code/manage.py runserver 0.0.0.0:8000
