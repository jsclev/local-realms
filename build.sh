#!/usr/bin/env bash

export PYTHONPATH=$(pwd):${PYTHONPATH}
export DJANGO_SETTINGS_MODULE=settings.settings

# Rebuild the database structure
rm db.sqlite3
python manage.py makemigrations finder
python manage.py migrate

# Populate the database
cd scripts
python populate.py
cd ..
