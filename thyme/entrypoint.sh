#!/usr/bin/env bash

alembic upgrade head
python manage_web.py
