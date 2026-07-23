.PHONY: extract transform load pipeline format test

extract:
	python -m etl.extract.extract_weather

transform:
	python -m etl.transform.transform_weather

load:
	python -m etl.load.load_weather

pipeline:
	python -m main

lint:
	ruff check .

format:
	black .
	isort .

test:
	PYTHONPATH=. python3 -m pytest 

type:
	PYTHONPATH=. python3 -m mypy \
		main.py \
		bootstrap.py \
		pipeline.py \
		clients \
		config \
		etl \
		models \
		repositories

quality:
	make lint
	make format
	make type
	make test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete