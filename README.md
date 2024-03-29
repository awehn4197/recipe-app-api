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

docker-compose run --rm app sh -c "python manage.py startapp user"

ssh ec2-user@<ip of ec2 instance>

sudo yum install git -y
sudo amazon-linux-extras install docker -y
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ec2-user

docker-compose -f docker-compose-deploy.yml up -d

docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py createsuperuser"

docker-compose -f docker-compose-deploy.yml logs

docker-compose -f docker-compose-deploy.yml build app

docker-compose -f docker-compose-deploy.yml up --no-deps -d app