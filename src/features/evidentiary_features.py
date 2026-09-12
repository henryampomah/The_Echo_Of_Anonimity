"""Evidentiary rigor features: links + evidentiary lexicon."""
import re
import pandas as pd
from urllib.parse import urlparse

DOMAIN_CREDIBILITY = {
    ".gov": 1.0, ".edu": 0.9, ".mil": 0.9,
    ".org": 0.7, ".int": 0.7,
    ".com": 0.5, ".net": 0.5, ".co": 0.4, ".uk": 0.4, ".eu": 0.4,
    ".news": 0.6, ".media": 0.5,
    ".info": 0.3, ".xyz": 0.1, ".biz": 0.2, ".cc": 0.2, ".tv": 0.3,
    ".blog": 0.3, ".wordpress": 0.3, ".medium": 0.4, ".substack": 0.4,
}
HIGH_CRED = {
    "wikipedia.org": 0.8, "bbc.com": 0.9, "bbc.co.uk": 0.9,
    "nytimes.com": 0.85, "washingtonpost.com": 0.85, "theguardian.com": 0.85,
    "reuters.com": 0.9, "apnews.com": 0.9, "npr.org": 0.85,
    "cnn.com": 0.7, "foxnews.com": 0.6, "msnbc.com": 0.65,
}

EVIDENTIARY_LEXICON = {
    "source_citation": [
        "according to", "cited", "source", "sources", "per", "via",
        "reported", "confirmed", "stated", "claimed", "alleged",
        "documented", "recorded", "verified", "fact-checked", "debunked",
        "corroborated", "substantiated", "unsubstantiated",
    ],
    "data_statistics": [
        "data", "statistics", "figures", "numbers", "percentage", "percent",
        "survey", "poll", "study", "research", "report", "analysis",
        "dataset", "sample", "methodology", "evidence", "proof",
        "empirical", "quantitative", "qualitative",
    ],
    "logical_reasoning": [
        "therefore", "thus", "hence", "consequently", "as a result",
        "because", "since", "given that", "assuming", "implies",
        "suggests", "indicates", "demonstrates", "proves", "concludes",
        "infers", "deduces", "follows", "contradicts",
    ],
    "comparison_contrast": [
        "compared to", "in contrast", "however", "nevertheless",
        "on the other hand", "whereas", "although", "despite",
        "similarly", "likewise",
    ],
    "certainty_uncertainty": [
        "clearly", "obviously", "certainly", "definitely", "undoubtedly",
        "possibly", "probably", "likely", "unlikely", "perhaps", "maybe",
        "seemingly", "apparently", "reportedly", "purportedly", "supposedly",
    ],
    "legal_human_rights": [
        "international law", "geneva convention", "war crime",
        "crimes against humanity", "human rights", "humanitarian law",
        "un resolution", "security council", "icj", "icc",
        "amnesty international", "human rights watch", "red cross",
        "ocha", "unrwa", "violation", "illegal", "unlawful", "legitimate",
    ],
    "verification_factcheck": [
        "fact-check", "misinformation", "disinformation", "propaganda",
        "fake news", "hoax", "misleading", "inaccurate", "false",
        "true", "accurate", "credible", "reliable", "biased",
        "objective", "impartial",
    ],
    "quantitative_units": [
        "casualties", "fatalities", "wounded", "displaced", "refugees",
        "deaths", "injuries", "destroyed", "demolished", "rockets",
        "airstrikes", "missiles", "troops", "soldiers", "militants",
        "civilians", "hostages", "prisoners", "thousands", "hundreds",
    ],
}

WEAK_RIGOR = [
    "trust me", "believe me", "obviously", "everyone knows",
    "common sense", "i feel", "i think", "in my opinion",
    "just saying", "wake up", "sheeple", "mainstream media",
    "msm", "deep state", "globalist",
]

ALL_EVIDENTIARY = [w for lst in EVIDENTIARY_LEXICON.values() for w in lst]

def _extract_urls(text):
    return re.findall(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])+", text or "")

def _credibility(url):
    try:
        d = urlparse(url).netloc.lower()
        if d.startswith("www."):
            d = d[4:]
        if d in HIGH_CRED:
            return HIGH_CRED[d]
        for tld, s in DOMAIN_CREDIBILITY.items():
            if d.endswith(tld):
                return s
        return 0.3
    except Exception:
        return 0.3

def _domain(url):
    try:
        return urlparse(url).netloc.lower()
    except ValueError:
        return ""

def _link_features(text):
    urls = _extract_urls(text)
    if not urls:
        return {"link_count": 0, "avg_domain_credibility": 0,
                "rigor_score": 0, "unique_domains": 0, "has_link": False}
    creds = [_credibility(u) for u in urls]
    return {
        "link_count":             len(urls),
        "avg_domain_credibility": sum(creds) / len(creds),
        "rigor_score":            len(urls) * (sum(creds) / len(creds)),
        "unique_domains":         len({_domain(u) for u in urls if _domain(u)}),
        "has_link":               True,
    }

def _lexicon_features(text):
    t = (text or "").lower()
    ev = 0
    for kw in ALL_EVIDENTIARY:
        ev += len(re.findall(r"\b" + re.escape(kw) + r"\b", t))
    weak = 0
    for kw in WEAK_RIGOR:
        weak += len(re.findall(r"\b" + re.escape(kw) + r"\b", t))
    wc = max(1, len(t.split()))
    return {
        "evidentiary_count":   ev,
        "weak_count":          weak,
        "rigor_lexicon_score": (ev - weak) / wc,
        "evidence_density":    ev / wc,
    }

def _all(raw_text, clean_text):
    # Link extraction MUST run on raw text — cleaned text has [URL] placeholders
    feats = _link_features(raw_text)
    # Lexicon scoring runs on cleaned text (removes noise)
    feats.update(_lexicon_features(clean_text))
    return feats


def add_evidentiary_features(df, raw_col="self_text", text_col="clean_text"):
    feats = df.apply(
        lambda r: _all(r.get(raw_col, "") or "", r.get(text_col, "") or ""),
        axis=1
    ).apply(pd.Series)
    return pd.concat([df, feats], axis=1)