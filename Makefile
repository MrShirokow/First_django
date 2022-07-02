all: makemigrations migrate run

makemigrations:
	python manage.py makemigrations

migrate:
	docker exec first_django_web_1 python manage.py migrate

run:
	docker-compose up
