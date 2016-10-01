# Django-SQL-sample

# install
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-test.txt
pip install -r requirements-travisci.txt

# create database
python manage.py makemigrations
python manage.py migrate

# start server
python manage.py runserver 0.0.0.0:8000
