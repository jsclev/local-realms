#!/usr/bin/env bash

export PYTHONPATH=$(pwd):${PYTHONPATH}
export DJANGO_SETTINGS_MODULE=settings.settings

# Make sure all Python dependencies are updated
pip install -r requirements.txt

# Rebuild the database structure
rm db.sqlite3
rm -rf apps/finder/migrations
python manage.py makemigrations finder
python manage.py migrate

# Populate the database
cd scripts
python populate.py
python populate_zip_codes.py
python populate_yelp_data.py
cd ..
