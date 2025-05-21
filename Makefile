dev:
	uv run fastapi dev --host 0.0.0.0 --port 8000

run:
	uv run fastapi run --host 0.0.0.0 --port 8000

lint:
	uv run ruff check --fix

format:
	uv run ruff format

ty:
	uv run ty check

ty-server:
	uv run ty server

test:
	uv run -m pytest
