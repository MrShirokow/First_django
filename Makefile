all: makemigrations migrate run

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
