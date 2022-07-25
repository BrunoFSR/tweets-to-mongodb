#!bin/sh
docker-compose up --build -d
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python TwitterStreamApp.py