# Model Card

**Status:** Model artifacts and saved metrics inspected; results not independently retrained  
**Last updated:** 2026-10-15

## Model and Intended Task

The project contains a supervised platform classifier implemented in `notebooks/04_computational_model.ipynb`. The primary saved artifact is a scikit-learn `RandomForestClassifier`; the notebook also compares Logistic Regression and an RBF-kernel SVM. The task is to predict the platform label (Reddit versus X) for rows in a balanced, feature-engineered sample. This is not a model of polarization, truth, evidence quality, anonymity, or user emotion.

The local files `results/tables/random_forest_model.joblib` and `scaler.joblib` are ignored by Git and are not available to a repository-only user. No model version, training-data snapshot, artifact checksum, or deployment interface is recorded.

## Inputs, Outputs, and Features

The notebook uses 26 available columns from a proposed feature list. Inputs include readability and lexical features; URL/domain and evidentiary-lexicon features; VADER/NRC-derived sentiment/emotion features; engagement measures; and temporal fields such as hour and day of week. Four proposed derived features are missing and omitted. The target is `platform`, coded as Reddit = 1 and X = 0.

Because engagement features are inputs, the model does **not** test the README's “linguistic features alone” framing. In the saved Random Forest result, `engagement_log` and `engagement_normalized` account for about 65.8% of reported feature importance. The classifier may largely identify the datasets through platform-specific engagement scales and metadata. Feature importance is model-specific association, not a causal explanation.

## Training and Evaluation Procedure

The notebook specifies a stratified 80/20 train/test split using random seed 42 and `StandardScaler` fitted on the training subset. It also computes five-fold cross-validation on the scaled training data. The notebook's model settings for the main Random Forest include 200 trees, maximum depth 15, minimum split size 10, minimum leaf size 5, and `n_jobs=-1`.

The notebook fills missing feature values using column means **before** the train/test split. This allows test-set distribution information into preprocessing and weakens the independence of the reported holdout evaluation. The separate feature-selection experiment also scales the full selected dataset before splitting. No nested validation or leakage-safe imputation pipeline is implemented in the inspected notebook.

## Saved Results

Values below are reported by `results/tables/model_results.json` and `model_comparison.csv`; they are cached results, not independently reproduced in this documentation task.

| Model/result source                                                 | Accuracy | Precision | Recall |     F1 |          ROC-AUC |
| ------------------------------------------------------------------- | -------: | --------: | -----: | -----: | ---------------: |
| Random Forest `performance` in `model_results.json`                 |   0.9867 |    0.9927 | 0.9806 | 0.9866 |           0.9993 |
| Random Forest entry in `model_comparison.csv` / embedded comparison |   0.9906 |    0.9966 | 0.9844 | 0.9905 |           0.9997 |
| Logistic Regression comparison                                      |   0.9997 |    0.9994 | 1.0000 | 0.9997 | 1.0000 (rounded) |
| RBF SVM comparison                                                  |   0.9969 |    0.9972 | 0.9967 | 0.9969 |           0.9999 |

The two reported Random Forest evaluations disagree. Treat all scores as unverified until the exact input Parquet artifact, notebook state, split, and saved model are regenerated and reconciled. Very high classification performance is not evidence of substantive validity and may reflect platform-specific metadata or sample construction.

## Limitations, Risks, and Intended Use

The labels are inherited from platform identity rather than human annotation. Samples are not shown to represent all Reddit or X content, and no external test set or temporal holdout is documented. The model is not independently evaluated for robustness, calibration, subgroup performance, concept drift, or sensitivity to engagement/time features. Error analysis is not available in the repository evidence inspected.

Lexical and readability measures can be affected by short texts, spelling, dialect, quoted content, URLs, and language detection. VADER and NRC outputs can miss sarcasm, negation, context, slang, multilingual content, and conflict-specific meanings. Automatically inferred sentiment/emotion values are not measurements of internal belief or intent.

**Intended use:** reproducing the exploratory platform-classification experiment after resolving data access and evaluation issues.  
**Not intended for:** moderation, user profiling, political persuasion, identifying individuals, truth assessment, or general claims about Reddit and X users.

## Reproduction Status

The project environment records Python 3.13.1 and pins packages in `requirements.txt`. The notebook and saved outputs were inspected; the model was not retrained in this documentation pass. The direct entry point `main.py` currently fails before modeling because `src.hypothesis_validation` is absent from the working tree. The test directory contains no tests. Do not treat the saved model binary as independently verified against the documented metrics.
