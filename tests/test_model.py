from unittest.mock import MagicMock

import model


def test_predict_empty():
    assert model.predict("") == ("(empty)", 0.0)
    assert model.predict("   ") == ("(empty)", 0.0)
    assert model.predict(None) == ("(empty)", 0.0)


def test_predict_with_clf(monkeypatch):
    pipe = MagicMock(return_value=[{"label": "NEGATIVE", "score": 0.951234}])
    monkeypatch.setattr(model, "get_clf", lambda: pipe)
    assert model.predict("bad") == ("NEGATIVE", 0.951)
    pipe.assert_called_once_with("bad")
