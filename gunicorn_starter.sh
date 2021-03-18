#!/bin/sh
python app.py db init
python app.py db migrate
python app.py db upgrade
gunicorn --bind 0.0.0.0:5000 app:app
