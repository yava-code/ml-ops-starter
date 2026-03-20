.PHONY: run test docker-build docker-run

run:
	pip install -r requirements.txt
	python app.py

test:
	pip install -r requirements-dev.txt
	pytest -q

docker-build:
	docker build -t sentiment-api .

docker-run:
	docker run --rm -p 7860:7860 sentiment-api
