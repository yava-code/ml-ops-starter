from transformers import pipeline

clf = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def predict(text):
    if not text or not str(text).strip():
        return "(empty)", 0.0
    res = clf(text)[0]
    return res["label"], float(round(res["score"], 3))
