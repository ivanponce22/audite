#!/bin/sh
python manage.py migrate --settings=audite.settings.prd
python manage.py collectstatic --no-input --settings=audite.settings.prd
