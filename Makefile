.PHONY: run logs down debug 

run:
	@COMPOSE_BAKE=true docker compose up -d --build

logs:
	@docker compose logs

down:
	@docker compose down
