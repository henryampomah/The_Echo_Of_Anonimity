"""Sentiment + emotion features.

WHY THIS FILE CHANGED
----------------------
The original version called HuggingFace transformer pipelines
(cardiffnlp/twitter-roberta-base-sentiment-latest and
j-hartmann/emotion-english-distilroberta-base). Those download multi-hundred-MB
model weights from the Hugging Face Hub the moment this module is imported.
In an environment without access to huggingface.co, every call to
_emotions() raised an exception and silently fell back to
{neutral: 1.0, everything else: 0.0} (see the bare `except Exception` block
in the old code). That produced sentiment_score == 0.0 and
sentiment_intensity == 0.0 for all 10,000 rows -- confirmed by the
"Reddit means / X means" output in 02_feature_engineering.ipynb, which showed
sentiment_score = 0.0000 exactly for both platforms. That's what invalidated
H3 (no variance to find a peak), H4 (regression returned NaN), and H5
(Granger causality fails on a constant series).

This version replaces the transformer pipelines with two well-established,
fully offline, pip-installable tools that need no network access at runtime:
  - VADER (vaderSentiment) for overall sentiment polarity -> sentiment_score
  - NRCLex (NRC Word-Emotion Association Lexicon) for the six discrete
    emotion categories (anger, disgust, fear, joy, sadness, surprise) that
    03_exploratory_data_analysis.ipynb and 04_computational_model.ipynb
    already reference by name.

Install once before rerunning the pipeline:
    pip install vaderSentiment NRCLex

Function signature and output columns are unchanged
(anger, disgust, fear, joy, neutral, sadness, surprise, sentiment_score,
sentiment_intensity), so no other notebook needs to change.
"""
import re
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nrclex import NRCLex

_vader = SentimentIntensityAnalyzer()

_EMO_LABELS = ["anger", "disgust", "fear", "joy", "neutral", "sadness", "surprise"]
_TOKEN_RE = re.compile(r"[a-zA-Z']+")


def _sentiment(text):
    """VADER compound score in [-1, 1]; positive = positive sentiment,
    same convention the old transformer-based version used."""
    if not isinstance(text, str) or len(text.strip()) < 5:
        return 0.0
    try:
        return float(_vader.polarity_scores(text)["compound"])
    except Exception as e:
        print(f"[sentiment error] {type(e).__name__}: {e} | input: {text[:60]!r}")
        return 0.0


def _emotions(text):
    """NRC-lexicon-based discrete emotion proportions. Fully offline --
    the lexicon ships bundled with the NRCLex package."""
    if not isinstance(text, str) or len(text.strip()) < 5:
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}
    try:
        tokens = _TOKEN_RE.findall(text.lower())
        if not tokens:
            return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}
        obj = NRCLex()
        obj.load_token_list(tokens)
        freq = obj.affect_frequencies
        out = {k: freq.get(k, 0.0) for k in
               ["anger", "disgust", "fear", "joy", "sadness", "surprise"]}
        out["neutral"] = max(0.0, 1.0 - sum(out.values()))
        return out
    except Exception as e:
        print(f"[emotion error] {type(e).__name__}: {e}")
        return {k: 0.0 for k in _EMO_LABELS} | {"neutral": 1.0}


def add_sentiment_features(df, text_col="clean_text"):
    print(f"[sentiment] computing on {len(df):,} rows ...")
    print("[sentiment] computing emotions (NRC lexicon) ...")
    emo = df[text_col].apply(_emotions).apply(pd.Series)
    result = pd.concat([df, emo], axis=1)

    print("[sentiment] computing polarity (VADER) ...")
    result["sentiment_score"] = df[text_col].apply(_sentiment)
    result["sentiment_intensity"] = 1.0 - result["neutral"]

    print(f"[sentiment] non-zero scores: {(result['sentiment_score'] != 0).sum():,}")
    return result