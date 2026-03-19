# sentiment-api

![CI](https://github.com/yava-code/sentiment-api/actions/workflows/ci.yml/badge.svg)

tiny gradio ui for sentiment (distilbert via transformers), docker + github actions.

## stack

- python + gradio + transformers
- docker
- github actions

## run local

```bash
pip install -r requirements.txt
python app.py
```

open http://127.0.0.1:7860

## docker

```bash
docker build -t sentiment-api .
docker run -p 7860:7860 sentiment-api
```

first start downloads the model, can take a bit.
