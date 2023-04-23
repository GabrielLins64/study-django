#!/bin/bash

# Polls app's mock data
python /code/manage.py loaddata \
question.json \
choice.json \
&& echo "Mocks do app POLLS carregou"
