#!/usr/bin/env bash

# kill any servers that may be running in the background 
sudo pkill -f runserver

# kill frontend servers if you are deploying any frontend
# sudo pkill -f tailwind
# sudo pkill -f node

cd /home/ubuntu/django-aws_cicd/

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

install requirements.txt
pip install -r /home/ubuntu/django-aws_cicd/requirements.txt

# run server
<<<<<<< HEAD
screen -d -m python3 manage.py runserver 0:8000
=======
screen -d -m python3 manage.py runserver 0:8000
>>>>>>> 9b032624ebbc1cb897feae06dd9936a2c25a05a6
