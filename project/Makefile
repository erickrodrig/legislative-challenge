install:
	poetry install

run-server:
	poetry run python -m manage runserver

migrations:
	poetry run python -m manage makemigrations

migrate:
	poetry run python -m manage migrate

superuser:
	poetry run python -m manage createsuperuser

new-install: install migrations migrate superuser run-server ;
