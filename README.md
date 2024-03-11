# recipe-app-api

docker build .

docker-compose build

docker-compose run --rm app sh -c "flake8"

docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose run --rm app sh -c "python manage.py test"

docker-compose up

github actions:
- deployment
- code linting
- unit tests


docker-compose run --rm app sh -c "python manage.py wait_for_db"

docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"

docker-compose run --rm app sh -c "python manage.py makemigrations"

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

docker volume ls

docker volume rm recipe-app-api_dev-db-data

docker-compose run --rm app sh -c "python manage.py createsuperuser"
