all: makemigrations migrate run

run:
	python3.10 manage.py runserver

makemigrations:
	python3.10 manage.py makemigrations

migrate:
	python3.10 manage.py migrate
