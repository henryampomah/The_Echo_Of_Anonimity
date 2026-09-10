"""
config.py
Central configuration for the Echo of Anonymity project.
Israel-Palestine Conflict Dataset
"""
from pathlib import Path
from datetime import datetime

# ------------------------------------------------------------------
# PROJECT PATHS
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_RAW       = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL  = PROJECT_ROOT / "data" / "external"

RESULTS         = PROJECT_ROOT / "results"
RESULTS_FIGURES = RESULTS / "figures"
RESULTS_TABLES  = RESULTS / "tables"

LOGS = PROJECT_ROOT / "logs"

for p in [DATA_RAW, DATA_PROCESSED, DATA_EXTERNAL,
          RESULTS_FIGURES, RESULTS_TABLES, LOGS]:
    p.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------
# RAW DATA FILES
# ------------------------------------------------------------------
REDDIT_RAW_FILE  = DATA_RAW / "reddit_israel_hamas.csv"
TWITTER_RAW_FILE = DATA_RAW / "X_israel_hamas_r.csv"

# ------------------------------------------------------------------
# EVENT DEFINITION
# ------------------------------------------------------------------
# Israel-Hamas war anchor event: October 7, 2023 attacks
EVENT_NAME        = "Israel-Hamas War (Oct 7, 2023)"
EVENT_START       = datetime(2023, 10, 7, 0, 0, 0)   # UTC
TIME_WINDOW_HOURS = 48 * 30   # 30 days of discourse — adjust as needed

# ------------------------------------------------------------------
# RAW COLUMN NAMES  (change here if your CSV headers change)
# ------------------------------------------------------------------
REDDIT_COLUMNS = {
    "id":           "comment_id",
    "text":         "self_text",
    "timestamp":    "created_time",
    "author":       "author_name",
    "subreddit":    "subreddit",
    "score":        "score",
    "ups":          "ups",
    "downs":        "downs",
    "controversial":"controversiality",
    "post_id":      "post_id",
    "post_title":   "post_title",
    "verified":     "user_is_verified",
    "account_created": "user_account_created_time",
    "total_karma":  "user_total_karma",
    "comment_karma":"user_comment_karma",
    "account_age":  "account_age_days",
    "post_score":   "post_score",
    "post_upvote_ratio": "post_upvote_ratio",
}

TWITTER_COLUMNS = {
    "text":         "tweet_text",
    "author":       "user",
    "timestamp":    "tweet_pub_time",
    "likes":        "tweet_likes",
    "replies":      "tweet_replies",
    "reposts":      "tweet_reposts",
    "tweets_num":   "tweets_num",
    "following":    "following_num",
    "followers":    "followers_num",
    "url":          "link",
}

# ------------------------------------------------------------------
# PRIORITY SUBREDDITS
# ------------------------------------------------------------------
PRIORITY_SUBREDDITS = {
    # === YOUR ORIGINAL LIST ===
    "politics", "worldnews", "conservative", "news", "worldpolitics",
    "geopolitics", "politicaldiscussion", "truereddit", "neutralpolitics",
    "palestine", "israel", "middleeastnews", "changemyview",
    "outoftheloop", "publicfreakout", "conspiracy",
    
    # === RECOMMENDED ADDITIONS ===
    # Direct conflict subreddits
    "IsraelPalestine", "Israel_Palestine", "Palestine", "Israel",
    "Gaza", "GazaStrip", "MiddleEast", "MiddleEastNews",
    
    # News & analysis
    "inthenews", "qualitynews", "moderatepolitics", "askpolitics",
    "politicalcompassmemes", "PoliticalCompassMemes",
    
    # International perspective
    "europe", "ukpolitics", "canadapolitics", "australianpolitics",
    "internationalpolitics", "GlobalTalk", "worldnews",
    
    # Academic/analytical
    "AskHistorians", "AskSocialScience", "geopolitics", "CredibleDefense",
    "warcollege", "LessCredibleDefence",
    
    # Debate & discussion
    "debate", "debateanatheist", "changemyview", "NeutralPolitics",
    "PoliticalDiscussion", "TrueReddit",
    
    # Media critique
    "media_criticism", "Journalism", "bannedfromnews",
    
    # Regional
    "arabs", "Arab", "jewish", "Judaism", "Islam",
    "muslim", "MuslimLounge", "exmuslim",
    
    # Diaspora
    "Jewish", "Israel", "Palestine", "Arab",
    
    # Conflict documentation
    "CombatFootage", "ukraine", "CombatVideos",
    "war", "Military", "MilitaryHistory"
}

# ------------------------------------------------------------------
# MODEL PARAMETERS
# ------------------------------------------------------------------
RANDOM_SEED = 42
TEST_SIZE   = 0.20
ALPHA       = 0.05

# Final feature list used by Phase 4 & 5 (must match engineered cols)
FEATURES = [
    # lexical
    "fk_grade", "fk_ease", "ttr", "avg_word_len", "avg_syllables",
    "gunning_fog", "coleman_liau", "automated_readability",
    # evidentiary
    "link_count", "avg_domain_credibility", "rigor_score",
    "evidence_density", "evidentiary_count", "weak_count",
    "rigor_lexicon_score",
    # sentiment / emotion
    "sentiment_score", "sentiment_intensity",
    "anger", "disgust", "fear", "joy", "sadness", "surprise",
    # engagement
    "engagement_raw", "engagement_log", "engagement_normalized",
    # temporal
    "hour", "day_of_week", "is_weekend", "hours_since_event",
]