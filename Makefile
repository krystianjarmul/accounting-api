build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down  --remove-orphans

tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /tests