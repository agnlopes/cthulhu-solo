coverage:
	poetry run pytest --cov=src tests --cov-report=html:coverage_html

test:
	poetry run pytest -q

test-coverage: coverage test

install:
	poetry install

clean:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf
	find . -name "cthulhu.*log" | xargs rm -f
