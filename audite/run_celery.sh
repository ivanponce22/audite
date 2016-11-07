#!/bin/sh
/usr/local/bin/celery --app=audite.celery:app worker --loglevel=INFO