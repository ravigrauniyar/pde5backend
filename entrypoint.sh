#!/bin/bash

source .env
python manage.py migrate
python manage.py runserver