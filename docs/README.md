Indonesian Weather Platform

An end-to-end Data Engineering project that collects weather data
from Open-Meteo API, validates, transforms,
and loads it into PostgreSQL Data Warehouse.

Features
--------

✔ ETL Pipeline
✔ Data Validation
✔ PostgreSQL Warehouse
✔ Repository Pattern
✔ Dependency Injection
✔ Docker Ready
✔ Ruff
✔ Black
✔ isort
✔ mypy
✔ pytest
✔ pre-commit

Architecture

API
        │
        ▼
Extractor
        │
        ▼
Validator
        │
        ▼
Transformer
        │
        ▼
Loader
        │
        ▼
PostgreSQL