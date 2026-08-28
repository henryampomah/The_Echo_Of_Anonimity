"""
Configuration file for the project
"""
import os
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent

# Data paths
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_EXTERNAL = PROJECT_ROOT / "data" / "external"

# Results paths
RESULTS = PROJECT_ROOT / "results"
RESULTS_FIGURES = RESULTS / "figures"
RESULTS_TABLES = RESULTS / "tables"

# Logs
LOGS = PROJECT_ROOT / "logs"

# Event details
EVENT_START = "2024-06-27 21:00:00"  # UTC
EVENT_NAME = "US Presidential Debate 2024"
TIME_WINDOW_HOURS = 48

# Platform configurations
PLATFORMS = {
    'reddit': {
        'name': 'Reddit',
        'subreddits': ['politics', 'news', 'worldnews', 'PoliticalDiscussion', 'conservative', 'liberal'],
        'data_file': DATA_RAW / 'reddit_comments.json'
    },
    'x': {
        'name': 'X',
        'data_file': DATA_RAW / 'x_twitter_dataset.csv'
    }
}

# Model parameters
RANDOM_SEED = 42
TEST_SIZE = 0.2

# Feature columns
FEATURES = [
    'fk_grade',
    'ttr',
    'avg_word_len',
    'rigor_score',
    'sentiment_score',
    'word_count',
    'link_count',
    'engagement_score'
]

# Hypothesis thresholds
ALPHA = 0.05
