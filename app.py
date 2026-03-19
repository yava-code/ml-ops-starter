# app.py
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
clf = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.get("/predict")
def predict(text: str):
    res = clf(text)[0]
    return {"label": res["label"], "score": round(res["score"], 3)}