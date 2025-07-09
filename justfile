# Default command - list all commands
default:
	just --list --unsorted

# fastapi
local:
	uv run --env-file .env.local fastapi dev --host 0.0.0.0 --port 8000

# fastapi run
run-local:
	uv run --env-file .env.local fastapi run --host 0.0.0.0 --port 8000

# ruff lint
lint:
	uv run ruff check --fix

# ruff format
format:
	uv run ruff format
	prettier --write .

# ty
ty:
	uv run ty check

# ty start server
ty-server:
	uv run ty server

########################################################
# DOCKER
########################################################

# docker compose
up:
	docker-compose up --build

# docker compose down
down:
	docker-compose down

########################################################
# TESTING
########################################################

# run unit tests
test-unit:
	uv run --env-file .env.local -m pytest tests/unit/ -v

# run integration tests
test-integration:
	uv run --env-file .env.local -m pytest tests/integration/ -v

# run end to end tests
test-e2e-local:
	uv run --env-file .env.local -m pytest tests/e2e/ -v

# run end to end tests
test-e2e: test-e2e-local

# run all tests
test: test-unit test-integration test-e2e