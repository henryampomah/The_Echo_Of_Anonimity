# Data Card: Reddit and X Political Discourse Datasets

## 1. Dataset Overview

### 1.1 Purpose

This data card documents the datasets used in the study, **“The Echo of Anonymity: A Multi-Modal Computational Analysis of Evidentiary Reasoning and Emotional Contagion in Political Polarization across Reddit and X.”**

The study examines political discourse relating to the Israel-Palestine conflict across Reddit and X (formerly Twitter). The analysis focuses on textual characteristics, sentiment, and hyperlink-related features, with the aim of comparing selected records from the two platforms.

This document records the datasets' origins, selection procedures, preprocessing steps, features, intended uses, limitations, and outstanding verification requirements. It is based on the information currently available about the project. Details that require confirmation from the repository, dataset metadata, or original documentation are explicitly marked as unverified.

### 1.2 Dataset Summary

| Attribute | Description |
|---|---|
| Study domain | Computational social media mining |
| Research topic | Political discourse surrounding the Israel-Palestine conflict |
| Platforms | Reddit and X |
| Dataset format | CSV |
| Data source | Kaggle |
| Total records used | 20,000 |
| Reddit records used | 10,000 |
| X records used | 10,000 |
| Reported period covered | October 2023 to November 2023 |
| Download date | August 2026 |
| Selection approach | Filtering followed by selection of 10,000 records from each dataset |
| Language filter | English-language records |
| Topic filter | Records containing keywords related to the research topic |
| Main analytical areas | Sentiment analysis, textual or lexical analysis, and hyperlink counting |
| Exact model used | Unknown; inspect the repository code and model configuration |
| Exact licence names | Require verification against the dataset pages and metadata |

The 20,000 records represent the samples used in this study, not the total sizes of the original Kaggle datasets.

## 2. Data Sources and Provenance

### 2.1 Reddit Dataset

- **Dataset name:** Reddit on Israel-Palestine (Daily Updated)
- **Provider:** Kaggle dataset contributor, `asaniczka`
- **Source URL:** https://www.kaggle.com/datasets/asaniczka/reddit-on-israel-palestine-daily-updated
- **Local filename:** `reddit_israel_hamas.csv`
- **Records used:** 10,000
- **Reported period covered by the study data:** October 2023 to November 2023
- **Primary text field used for analysis:** `self_text`

The Reddit dataset provides records associated with discussions about the Israel-Palestine conflict. The available columns include comment information, subreddit information, post information, user-related attributes, and engagement-related measures.

**Verification required:** The original dataset's complete record count, precise collection period, collection procedure, collection frequency, and the provider's definition of each field have not yet been independently confirmed. These details should be checked against the dataset documentation and repository files.

### 2.2 X Dataset

- **Dataset name:** Tweets: Israeli-Palestinian Conflict / Gaza War
- **Provider:** Kaggle dataset contributor, `laidkahloul`
- **Source URL:** https://www.kaggle.com/datasets/laidkahloul/tweets-sraeli-palestinian-conflict-gazawar
- **Local filename:** `X_israel_hamas_r.csv`
- **Records used:** 10,000
- **Reported period covered by the study data:** October 2023 to November 2023
- **Primary text field used for analysis:** `tweet_text`

The X dataset contains post text and associated fields relating to publication time, engagement, user activity, and links.

**Verification required:** The original dataset's complete record count, exact collection dates, collection method, and field definitions must be confirmed using the provider's documentation and the downloaded CSV file.

### 2.3 Original Data Collection

The datasets were obtained from Kaggle in August 2026. The original data collection methods are attributed to the respective dataset providers, but the precise methods have not yet been established.

The project team did not report independently collecting new records through platform APIs or web scraping for this analysis. This does not establish how the original dataset providers obtained their data.

Before publication, the repository documentation should identify the collection methods stated by each provider, where that information is available.

## 3. Dataset Composition and Features

### 3.1 Reddit Features

The reported columns in `reddit_israel_hamas.csv` are:

| Feature | Description |
|---|---|
| `comment_id` | Identifier associated with a Reddit comment |
| `score` | Score associated with a record; precise meaning should be confirmed |
| `self_text` | Comment text field used in the analysis |
| `subreddit` | Subreddit associated with the record |
| `created_time` | Creation-time field; timestamp format requires verification |
| `post_id` | Identifier associated with the parent post |
| `author_name` | Author name or username field |
| `controversiality` | Field associated with the comment's controversiality |
| `ups` | Upvote-related field; precise interpretation requires verification |
| `downs` | Downvote-related field; precise interpretation requires verification |
| `user_is_verified` | User verification indicator |
| `user_account_created_time` | User account creation-time field |
| `user_awardee_karma` | Awardee karma field |
| `user_awarder_karma` | Awarder karma field |
| `user_link_karma` | Link karma field |
| `user_comment_karma` | Comment karma field |
| `user_total_karma` | Total karma field |
| `post_score` | Score associated with the post |
| `post_self_text` | Text associated with the post |
| `post_title` | Title of the post |
| `post_upvote_ratio` | Post upvote-ratio field |
| `post_thumbs_ups` | Post thumbs-up field |
| `post_total_awards_received` | Total awards received by the post |
| `post_created_time` | Post creation-time field |
| `account_age_days` | Account age expressed in days, according to the field name |

The field descriptions above are based on the column names and their apparent meanings. Their exact definitions, data types, units, and missing-value conventions should be checked against the actual data and provider documentation.

### 3.2 X Features

The reported columns in `X_israel_hamas_r.csv` are:

| Feature | Description |
|---|---|
| `user` | User identifier or username field; exact representation requires verification |
| `tweet_pub_time` | Publication-time field |
| `tweet_text` | Post text used in the analysis |
| `link` | Link field associated with the post |
| `tweet_likes` | Number of likes recorded for the post |
| `tweet_replies` | Number of replies recorded for the post |
| `tweet_reposts` | Number of reposts recorded for the post |
| `tweets_num` | User-related tweet count field; exact definition requires verification |
| `following_num` | Number of accounts followed, according to the field name |
| `followers_num` | Number of followers, according to the field name |

These descriptions should be treated as provisional until the column definitions and data types are checked.

### 3.3 Platform Feature Mapping

The main text fields selected for the platform comparison are:

| Platform | Source field | Analytical role |
|---|---|---|
| Reddit | `self_text` | Textual analysis and sentiment analysis |
| X | `tweet_text` | Textual analysis and sentiment analysis |

Using one primary text field per platform establishes a consistent starting point for comparing text. However, Reddit comments and X posts are different forms of user-generated content. They may differ in length, conversational context, structure, and intended audience.

The selected text fields should therefore not be assumed to be perfectly equivalent. The repository should also be checked to confirm whether empty `self_text` values were excluded and whether any additional text validation was performed.

## 4. Data Selection and Sampling

### 4.1 Selection Criteria

Records were selected using two main filters:

1. **Language filter:** Records identified as English-language content.
2. **Topic filter:** Records containing keywords related to the Israel-Palestine conflict and the study topic.

The filters were implemented in project code rather than relying exclusively on filtering performed by the original dataset providers.

**Verification required:** The exact keyword list, the method used to identify English-language records, the handling of ambiguous matches, and whether the filters were identical across both platforms must be confirmed by inspecting the code.

### 4.2 Sample Size

The final analytical sample contained 20,000 records:

- 10,000 Reddit records.
- 10,000 X records.

The 10,000-record selection from each platform was made after cleaning and filtering, according to the project's reported workflow. All records within each selected 10,000-record sample were then included in the analysis.

The original dataset sizes and the number of records remaining after each processing stage have not yet been established.

### 4.3 Sampling Method

The sampling approach involved filtering records by language and topic, cleaning the resulting data, and selecting 10,000 records from each platform.

The exact method used to select the 10,000 records is not yet documented here. In particular, it is unknown whether selection was random, chronological, based on file order, or determined by another rule.

The repository code should be inspected to establish:

- Whether selection was random or deterministic.
- Whether a random seed was used.
- Whether records were selected chronologically or by file order.
- Whether the selection procedure could introduce bias.
- Whether the same selection logic was applied to both datasets.

Until these details are confirmed, the samples should not be described as random or statistically representative.

## 5. Data Cleaning and Preprocessing

The reported preprocessing operations were:

1. **Missing and empty record removal:** Records with missing or empty data relevant to the processing workflow were removed. The exact columns checked and the handling of partially missing records require verification.
2. **Duplicate removal:** Duplicate records were removed. The columns used to identify duplicates and whether deduplication occurred before or after filtering require confirmation from the code.
3. **Lowercase conversion:** Text was converted to lowercase.
4. **Stop-word removal:** Stop words were removed from the text.

The 10,000-record samples were selected after cleaning and filtering.

### 5.1 Preprocessing Considerations

These transformations can influence the results of textual and sentiment analysis.

- **Lowercase conversion** reduces differences caused solely by capitalisation but removes capitalisation information that might otherwise convey emphasis.
- **Stop-word removal** can reduce the contribution of common words to lexical analysis. Depending on the stop-word list, it can also remove negation terms or other words important for interpreting sentiment.
- **Duplicate removal** can reduce repeated records, but it may also remove genuine repeated expressions or repost-like activity, depending on the definition of a duplicate.
- **Missing-value removal** can affect the distribution of the final sample if records with missing text or other fields differ systematically from retained records.

The exact implementation of each operation, including the stop-word list, text-processing library, duplicate criteria, and order of operations, should be recorded after inspection of the repository code.

No additional preprocessing operations have been confirmed.

## 6. Intended Uses

The datasets were selected for research and educational analysis of political discourse across Reddit and X.

The confirmed analytical areas are:

### 6.1 Sentiment Analysis

The study examines sentiment in the selected textual records.

**Model details:** The exact model, library, version, sentiment categories, and classification procedure have not yet been identified. These must be established from the repository code and model configuration.

The card should be updated with the model's name and version, input requirements, output labels, and any relevant validation results once verified.

### 6.2 Textual and Lexical Analysis

The text fields are used to examine textual characteristics across the two platforms.

The exact lexical measures, tokenisation method, statistical procedures, and comparison metrics require confirmation from the analysis code. No specific lexical findings or performance results are asserted in this data card.

### 6.3 Hyperlink Counting

The project includes analysis of hyperlinks or link-related features.

The confirmed procedure is hyperlink counting. A count of hyperlinks, or a measure of hyperlink frequency, does **not** independently establish the credibility, accuracy, reliability, or evidentiary quality of the linked sources.

Although source credibility appears in the broader research framing, a claim that the project evaluated source credibility would require additional documented procedures, such as an explicit credibility classification method or a validated source-evaluation framework. No such procedure has been confirmed here.

### 6.4 Other Potential Analyses

Engagement measures and timestamps are present in the reported dataset columns. Their availability does not, by itself, establish that they were used in the final analysis.

Temporal analysis, engagement analysis, emotion classification, political stance classification, and topic modelling are not listed as confirmed analytical procedures in this data card.

## 7. Known Limitations and Potential Biases

### 7.1 Selection Bias

The datasets were filtered by English language and topic-related keywords. This excludes content that does not match the filters, including relevant discussions that use different terminology, other languages, indirect references, or spelling variations.

The resulting samples represent records selected by the project's criteria rather than the full range of political discussion on either platform.

### 7.2 Platform Differences

Reddit comments and X posts differ in format and conversational context. Reddit records may also be associated with subreddit communities and parent posts, while X records include post-specific and user-related features.

Differences observed between the two samples may reflect these structural differences as well as differences in user expression. The data alone does not establish that platform anonymity caused any observed differences.

### 7.3 Unequal Meaning of Engagement Features

The datasets contain different engagement-related fields. Reddit includes fields such as scores, upvote ratios, and post-related measures, while X includes likes, replies, and reposts.

These measures are not necessarily equivalent. Comparisons should use clearly defined and justified measures rather than assuming that similarly named or related fields have identical meanings.

### 7.4 Time Coverage

The reported period covered is October 2023 to November 2023. This represents a specific period of political discourse and should not be treated as representative of discussions across all periods of the conflict.

The exact earliest and latest timestamps in each final sample should be calculated from the data and recorded after verification.

### 7.5 Data Quality

Removing missing records and duplicates does not guarantee that the remaining records are accurate, complete, or representative. The original datasets may contain classification errors, incomplete metadata, inaccurate timestamps, or other provider-specific limitations.

The actual frequency of such issues has not yet been measured in this data card.

### 7.6 Model Limitations

The exact analytical model and configuration remain unverified. Consequently, this document makes no claims about model accuracy, reliability, training data, calibration, or suitability for political discourse.

These details should be documented after inspecting the relevant code and configuration files.

### 7.7 Limits on Generalisation

The results should be interpreted as findings about the selected records and the implemented analysis. They should not automatically be generalised to all Reddit users, all X users, all English-language political discourse, or the wider population.

## 8. Privacy, Ethics, and Responsible Use

The reported datasets include user-related fields, including `author_name` in the Reddit data and `user` in the X data. They also include account-related and engagement-related attributes.

The presence of these fields creates potential privacy considerations even when data is publicly accessible.

The project should therefore:

- Use user identifiers only when necessary for the stated research objectives.
- Avoid publishing usernames, account identifiers, or unnecessary profile-level information in reports and figures.
- Review whether quoted posts or comments could be traced back to individual accounts.
- Avoid making unsupported inferences about the beliefs, identities, or intentions of individual users.
- Describe sentiment model outputs as analytical classifications rather than definitive evidence of a person's beliefs or intentions.
- Ensure that any released data and derived outputs comply with the applicable dataset terms and platform requirements.

The project-specific ethics approval status, any institutional review requirements, and the exact measures taken to protect identifiers have not been established in this data card. These details should be recorded accurately in the project's ethics documentation.

## 9. Licensing and Data Sharing

The project team reports checking the dataset licences and sharing conditions and determining that they permit the intended use and sharing.

However, the exact licence names, licence versions, and applicable conditions have not yet been recorded in this document.

Before redistributing the datasets or uploading copies of the raw CSV files to GitHub, verify the licence and terms for each dataset independently. The fact that a dataset is publicly accessible or downloadable from Kaggle does not, on its own, establish permission to redistribute it.

The repository should record:

- The exact licence stated for each dataset.
- The source of the licence information.
- Any attribution requirements.
- Any restrictions on redistribution or commercial use.
- Whether the original files may be shared or only the code and derived results may be published.

Until this verification is complete, the original CSV files should not be assumed to be freely redistributable.

## 10. Reproducibility and Repository Requirements

The following items should be documented or verified in the project repository to support reproducibility:

| Item | Current status |
|---|---|
| Original Kaggle dataset URLs | Known |
| Local CSV filenames | Known |
| Download month and year | August 2026 |
| Number of records used per platform | Known: 10,000 each |
| Reported study period | October to November 2023 |
| English-language and keyword filtering | Reported as implemented in code |
| Exact filtering keywords | Requires code inspection |
| Missing and empty record removal | Reported as performed |
| Duplicate removal | Reported as performed |
| Lowercase conversion | Reported as performed |
| Stop-word removal | Reported as performed |
| Exact stop-word list | Requires code inspection |
| Exact deduplication criteria | Requires code inspection |
| Exact sampling algorithm | Requires code inspection |
| Random seed, if applicable | Requires code inspection |
| Original and intermediate record counts | Requires code inspection or data audit |
| Exact model and version | Requires code and configuration inspection |
| Model output labels and configuration | Requires code inspection |
| Hyperlink-counting implementation | Requires code inspection |
| Exact dataset licences | Requires metadata verification |
| Original collection methods | Requires provider documentation |
| Package and dependency versions | Requires environment or dependency-file inspection |
| Ethics approval and identifier-handling measures | Requires project documentation |

For reproducibility, the repository should include the relevant processing scripts, dependency information, configuration files, and instructions for reproducing the selected samples and analytical outputs, subject to the applicable licence and privacy restrictions.

If the original CSV files cannot be redistributed, the repository can document their source URLs, required filenames, expected columns, and preparation procedure instead.

## 11. Outstanding Verification Checklist

The following checklist identifies work that remains before the data card can be considered fully verified.

- [ ] Confirm the original number of records in each downloaded dataset.
- [ ] Confirm the earliest and latest timestamps in each final sample.
- [ ] Record the exact English-language detection method.
- [ ] Record the complete list of topic-related keywords.
- [ ] Confirm the exact order of filtering, cleaning, deduplication, and sampling operations.
- [ ] Confirm the method used to select 10,000 records from each dataset.
- [ ] Record the number of records remaining after each processing stage.
- [ ] Confirm the exact fields used to identify duplicate records.
- [ ] Record the stop-word list and preprocessing implementation.
- [ ] Identify the exact sentiment model, version, and output labels.
- [ ] Confirm how hyperlinks were identified and counted.
- [ ] Confirm the licence and sharing conditions for each dataset.
- [ ] Document the original collection methods stated by the dataset providers.
- [ ] Confirm the project's privacy, ethics, and data-sharing arrangements.
- [ ] Verify the package versions and other environment details needed to reproduce the analysis.

## 12. Summary

This study uses two Kaggle datasets containing Reddit and X records relating to the Israel-Palestine conflict. The final analytical sample consists of 20,000 records, comprising 10,000 records from each platform, with a reported study period of October to November 2023.

The records were filtered for English-language content and topic-related keywords, cleaned to remove missing or empty records and duplicates, converted to lowercase, and processed to remove stop words. The main confirmed analytical areas are sentiment analysis, textual or lexical analysis, and hyperlink counting.

The datasets provide a basis for comparing selected political discourse across two social media platforms. However, sampling choices, differences in platform structure, incomplete knowledge of the original collection methods, and unverified model configuration limit the conclusions that can be drawn without further investigation.

This data card should be updated as the repository code, dataset metadata, model configuration, and licence information are verified. Unknown details should remain explicitly marked as unknown until supporting evidence is available.
