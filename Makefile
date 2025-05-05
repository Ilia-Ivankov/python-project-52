build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi

install:
	uv sync

collectstatic:
	uv run python manage.py collectstatic --noinput

migrate:
	uv run python manage.py migrate

lint:
	uv run flake8 task_manager

test:
	uv run python manage.py test task_manager.tests

run:
	uv run python manage.py runserver
