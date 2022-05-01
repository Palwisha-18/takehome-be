#!/bin/sh


python manage.py makemigrations
python manage.py migrate
echo 'Importing house data'
python manage.py import_house_data
exec "$@"