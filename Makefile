
install:
	uv venv
	uv pip install -e .
	uv pip install -e ./packages/pages
	uv run python manage.py migrate
	npm install

update:
	uv pip install -e .
	uv pip install -e ./packages/lineo-pages

run:
	uv run python manage.py runserver
