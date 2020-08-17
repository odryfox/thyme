#!/bin/sh

alembic upgrade head
python manage_web.py
