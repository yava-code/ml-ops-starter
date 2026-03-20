_clf = None


def get_clf():
    global _clf
    if _clf is None:
        from transformers import pipeline

        _clf = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
        )
    return _clf


def predict(text):
    if not text or not str(text).strip():
        return "(empty)", 0.0
    res = get_clf()(text)[0]
    return res["label"], float(round(res["score"], 3))
