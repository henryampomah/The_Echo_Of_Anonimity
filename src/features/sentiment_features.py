"""Sentiment + emotion features."""
from typing import Any, cast

import torch
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

_DEVICE = 0 if torch.cuda.is_available() else -1

_sent = cast(Any, pipeline)(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=_DEVICE,
)

_emo_name = "j-hartmann/emotion-english-distilroberta-base"
_emo_tok = AutoTokenizer.from_pretrained(_emo_name)
_emo_mod = AutoModelForSequenceClassification.from_pretrained(_emo_name)
_emo_mod.eval()
if _DEVICE == 0:
    _emo_mod = _emo_mod.to("cuda")

_EMO_LABELS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]

def _sentiment(text):
    if not text or len(text) < 5:
        return 0.0
    t = text[:512]
    try:
        r = _sent(t)[0]
        m = {"LABEL_0": -1, "LABEL_1": 0, "LABEL_2": 1}
        return m[r["label"]] * r["score"]
    except Exception:
        return 0.0

def _emotions(text):
    if not text or len(text) < 5:
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}
    try:
        inp = _emo_tok(text[:512], return_tensors="pt", truncation=True, max_length=512)
        if _DEVICE == 0:
            inp = {k: v.to("cuda") for k, v in inp.items()}
        with torch.no_grad():
            logits = _emo_mod(**inp).logits
        p = torch.nn.functional.softmax(logits, dim=-1)[0].cpu().tolist()
        return dict(zip(_EMO_LABELS, p))
    except Exception:
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}

def add_sentiment_features(df, text_col="clean_text"):
    df["sentiment_score"] = df[text_col].apply(_sentiment)
    df["sentiment_intensity"] = df["sentiment_score"].abs()
    emo = df[text_col].apply(_emotions).apply(pd.Series)
    return pd.concat([df, emo], axis=1)