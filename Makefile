install:
	poetry install

run-server:
	poetry run python -m project.manage runserver

migrations:
	poetry run python -m project.manage makemigrations

migrate:
	poetry run python -m project.manage migrate

superuser:
	poetry run python -m project.manage createsuperuser

new-install: install migrations migrate superuser run-server ;
