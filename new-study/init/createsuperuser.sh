#!/bin/bash

python /code/manage.py migrate && \
python /code/manage.py createsuperuser --noinput
