.PHONY: up debug down

up:
	@COMPOSE_BAKE=true docker compose up -d --build

down:
	@docker compose down

debug:
	@docker compose -f docker-compose.yaml -f docker-compose.debug.yaml up -d --build
