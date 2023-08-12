#!/usr/bin/env bash
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 crowdfunding.wsgifly volumes create -a fly-builder-bitter-hill-7413 -r syd --size 1 dbvol
