.PHONY: run docker-build docker-run

run:
	pip install -r requirements.txt
	python app.py

docker-build:
	docker build -t sentiment-api .

docker-run:
	docker run --rm -p 7860:7860 sentiment-api
