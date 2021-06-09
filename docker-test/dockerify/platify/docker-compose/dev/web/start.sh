python ./docker-compose/dev/web/wait_db.py
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
