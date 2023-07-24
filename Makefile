install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib test_*.py

lint:
	pylint --disable=W,C mylib/*.py *.py

format:
	black mylib/*.py *.py

all: install test lint format
