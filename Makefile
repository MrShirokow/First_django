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

superuser:
	docker exec -it 20be1f0231d6 python manage.py createsuperuser

cronadd:
	docker exec -it 20be1f0231d6 python manage.py crontab add
cronshow:
	docker exec -it 20be1f0231d6 python manage.py crontab show
cronremove:
	docker exec -it 20be1f0231d6 python manage.py crontab remove