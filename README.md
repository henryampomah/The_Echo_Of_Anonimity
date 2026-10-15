# The Echo of Anonymity: Computational Analysis of Political Discourse

## Project Overview
This research analyzes how platform affordances (anonymity, threading, visibility curation) shape political discourse quality on Reddit and X (Twitter) during major polarizing events.

## Project Structure
\\\
THE_ECHO_OF_ANONIMITY-1/
├── data/
│   ├── raw/              # Original, unprocessed datasets
│   ├── processed/        # Cleaned and feature-engineered data
│   └── external/         # External data (domain credibility, etc.)
├── notebooks/
│   ├── 01_data_preprocessing.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   ├── 03_hypothesis_validation.ipynb
│   └── 04_computational_model.ipynb
├── src/
│   ├── data_processing/  # Data loading and cleaning scripts
│   ├── features/         # Feature engineering
│   ├── models/           # Machine learning models
│   └── visualization/    # Plotting functions
├── results/
│   ├── figures/          # Generated plots
│   └── tables/           # Summary tables
├── logs/                 # Processing logs
├── tests/                # Unit tests
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── LICENSE
└── README.md
\\\

## Installation
\\\ash
pip install -r requirements.txt
\\\

## Data Sources
- Reddit: Pushshift API (archived comments)
- X (Twitter): HuggingFace datasets (tweets)

## Research Questions
1. How do platform affordances moderate lexical complexity in political discourse?
2. Does evidentiary reasoning differ between Reddit and X?

4. Can we predict platform from linguistic features alone?


