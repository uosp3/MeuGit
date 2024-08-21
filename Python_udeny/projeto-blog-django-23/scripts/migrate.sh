#!/bin/sh

makemigrations
echo 'Executando migrate.sh'
python manage.py migrate --noinput