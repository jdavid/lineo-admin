
install:
	uv venv
	#uv pip install -e .
	uv pip install -e ./packages/admin
	uv pip install -e ./packages/pages
	npm install

createsuperuser:
	uv run python manage.py createsuperuser

migrate:
	uv run python manage.py migrate

run:
	uv run python manage.py runserver
