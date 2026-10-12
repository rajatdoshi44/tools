start-weather:
	@echo "Starting the weather app..."
	uv run uvicorn apps.weather.main:app --reload --port 8081

start-all:
	@echo "Starting all apps..."
	$(MAKE) start-weather