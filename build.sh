#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Ensure the local upload folder structure exists on Render's drive so it doesn't throw a path error
mkdir -p media/task_images