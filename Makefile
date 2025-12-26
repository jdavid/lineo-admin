
install:
	npm install
	uv venv
	uv sync

createsuperuser:
	uv run python manage.py createsuperuser

migrate:
	uv run python manage.py migrate

run:
	uv run python manage.py runserver

shell:
	uv run python manage.py shell

outdated:
	uv pip list --outdated

update:
	uv sync -U
