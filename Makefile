build-dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml build

up-dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml up

down-dev:
	docker compose -f docker-compose.yml -f docker-compose.dev.yml down
