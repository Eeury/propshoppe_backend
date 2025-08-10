#!/usr/bin/env bash
set -o errexit 

pip install --upgrade pip
pip install -r requirements.txt
pip install setuptools

# Collect static files
python manage.py collectstatic --noinput
