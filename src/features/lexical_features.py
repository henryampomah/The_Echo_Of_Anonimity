"""Lexical complexity features."""
import pandas as pd

import re
import textstat

_ZERO_FEATURES = {
    "fk_grade": 0, "fk_ease": 0, "ttr": 0, "avg_word_len": 0,
    "avg_syllables": 0, "gunning_fog": 0,
    "coleman_liau": 0, "automated_readability": 0,
}

# Matches real words (letters + optional apostrophes), ignoring punctuation/numbers.
_WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")


def _safe_textstat_value(metric_name, default_value, *args):
    func = getattr(textstat, metric_name, None)
    if func is None:
        return default_value
    try:
        return func(*args)
    except Exception:
        return default_value


def compute_lexical_features(text):
    if not isinstance(text, str):
        return dict(_ZERO_FEATURES)

    # Clean tokens: strip punctuation, normalize case.
    words = _WORD_RE.findall(text.lower())
    if len(words) < 5:
        return dict(_ZERO_FEATURES)

    try:
        n = len(words)
        total_chars = sum(len(w) for w in words)
        syllable_counter = getattr(textstat, "syllable_count", None)
        total_syllables = sum(syllable_counter(w) for w in words) if syllable_counter else 0

        return {
            "fk_grade":              _safe_textstat_value("flesch_kincaid_grade", 0, text),
            "fk_ease":               _safe_textstat_value("flesch_reading_ease", 0, text),
            "ttr":                   len(set(words)) / n,
            "avg_word_len":          total_chars / n,
            "avg_syllables":         total_syllables / n,
            "gunning_fog":           _safe_textstat_value("gunning_fog", 0, text),
            "coleman_liau":          _safe_textstat_value("coleman_liau_index", 0, text),
            "automated_readability": _safe_textstat_value("automated_readability_index", 0, text),
        }
    except Exception:
        # Log the error in real code instead of swallowing it silently.
        return dict(_ZERO_FEATURES)

def add_lexical_features(df, text_col="clean_text"):
    feats = df[text_col].apply(compute_lexical_features).apply(pd.Series)
    return pd.concat([df, feats], axis=1)