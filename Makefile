build:
	docker-compose -f docker-compose.dev.yml build --pull

up:
	docker-compose -f docker-compose.dev.yml up -d

down:
	docker-compose -f docker-compose.dev.yml down -v

start: build up

isort:
	isort .

pylint:
	mypy thyme --ignore-missing-imports
