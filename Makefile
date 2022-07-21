all: makemigrations migrate up

makemigrations:
	python manage.py makemigrations

migrate:
	docker exec first_django_web_1 python manage.py migrate

up:
	docker-compose up

down:
	docker-compose down

build:
	docker-compose build

imageprune:
	docker image prune -f

superuser:
	docker exec -it first_django_web_1 python manage.py createsuperuser

cronadd:
	(crontab -l ; echo "*/1 * * * * docker exec first_django_web_1 bash ./cron.sh") | crontab -

cronshow:
	crontab -l

cronremove:
	crontab -r
