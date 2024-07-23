#!/usr/bin/env bash

set -o errexit


pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input


python manage.py migrate