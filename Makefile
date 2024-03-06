test:
	poetry run pytest --cov=src tests --cov-report=html:coverage_html

install:
	poetry install

