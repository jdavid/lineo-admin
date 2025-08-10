
install:
	uv venv venv313
	python manage.py migrate
