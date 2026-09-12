"""Sentiment + emotion features."""
import torch
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

_DEVICE = 0 if torch.cuda.is_available() else -1
print(f"[sentiment] device = {'GPU' if _DEVICE == 0 else 'CPU'}")

_sent = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    device=_DEVICE,
)

# probe once
_probe = _sent("This is a test of the sentiment pipeline.")
print(f"[sentiment] probe -> {_probe}")

_emo_name = "j-hartmann/emotion-english-distilroberta-base"
_emo_tok = AutoTokenizer.from_pretrained(_emo_name)
_emo_mod = AutoModelForSequenceClassification.from_pretrained(_emo_name)
_emo_mod.eval()
if _DEVICE == 0:
    _emo_mod = _emo_mod.to("cuda")

_EMO_LABELS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]

# map labels from the RoBERTa sentiment model
_LABEL_MAP = {
    "LABEL_0": -1, "negative": -1,
    "LABEL_1": 0,  "neutral": 0,
    "LABEL_2": 1,  "positive": 1,
}


def _sentiment(text):
    if not isinstance(text, str) or len(text.strip()) < 5:
        return 0.0
    try:
        r = _sent(text[:512])[0]
        return _LABEL_MAP[r["label"]] * float(r["score"])
    except Exception as e:
        print(f"[sentiment error] {type(e).__name__}: {e} | input: {text[:60]!r}")
        return 0.0


def _emotions(text):
    if not isinstance(text, str) or len(text.strip()) < 5:
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}
    try:
        inp = _emo_tok(text[:512], return_tensors="pt",
                       truncation=True, max_length=512)
        if _DEVICE == 0:
            inp = {k: v.to("cuda") for k, v in inp.items()}
        with torch.no_grad():
            logits = _emo_mod(**inp).logits
        p = torch.nn.functional.softmax(logits, dim=-1)[0].cpu().tolist()
        return dict(zip(_EMO_LABELS, p))
    except Exception as e:
        print(f"[emotion error] {type(e).__name__}: {e}")
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}


def add_sentiment_features(df, text_col="clean_text"):
    print(f"[sentiment] computing on {len(df):,} rows ...")
    df["sentiment_score"] = df[text_col].apply(_sentiment)
    df["sentiment_intensity"] = df["sentiment_score"].abs()
    print(f"[sentiment] non-zero scores: {(df['sentiment_score'] != 0).sum():,}")

    print("[sentiment] computing emotions ...")
    emo = df[text_col].apply(_emotions).apply(pd.Series)
    return pd.concat([df, emo], axis=1)