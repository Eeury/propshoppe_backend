#!/usr/bin/env bash
set -o errexit  # Exit on error

# Upgrade pip first (avoids install errors with some packages)
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
pip install setuptools

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput
