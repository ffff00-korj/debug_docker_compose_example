.PHONY: up debug down

run:
	@COMPOSE_BAKE=true docker compose up -d --build

logs:
	@docker compose logs

down:
	@docker compose down

debug:
	@docker compose -f docker-compose.yaml -f docker-compose.debug.yaml up -d --build
