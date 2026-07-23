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