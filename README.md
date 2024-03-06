# recipe-app-api

docker build .

docker-compose build

docker-compose run --rm app sh -c "flake8"

docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose up

github actions:
- deployment
- code linting
- unit tests