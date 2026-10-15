# Reproducibility Checklist

**Status:** Partial local artifact verification; full pipeline not reproduced  
**Last updated:** 2026-10-15

This checklist describes what is present and what was checked in this checkout. `[x]` means verified for the narrow statement written, not that the entire research result has been reproduced. `[ ]` means incomplete or not verified. `N/A` is reserved for genuinely inapplicable items.

## Project Framing and Source Versions

The current [`README.md`](../README.md) uses the title “The Echo of Anonymity: Computational Analysis of Political Discourse” and frames questions about platform affordances, lexical complexity, evidentiary reasoning, and platform prediction. The research prompt supplied for this documentation uses the expanded title “The Echo of Anonymity: A Multi-Modal Computational Analysis of Evidentiary Reasoning and Emotional Contagion in Political Polarization across Reddit and X” and a broader question centered on anonymity and temporal propagation. The code does not directly measure anonymity or emotional contagion, so the expanded framing is not evidence that those constructs were tested.

The current checkout also differs from research drafts available only in the Git index: the indexed hypothesis draft describes 5,000 observations per platform and four hypotheses with different results, while current notebooks and `complete_results.json` describe 9,000 per platform and five hypotheses. The indexed report also reports values that do not match current saved outputs. Those drafts are not present as working-tree files and are not treated as authoritative results here. A researcher should identify the intended final title, research question, and frozen analysis version before submission.

## Environment and Dependencies

- [x] A local Python virtual environment runs Python 3.13.1 (verified 2026-10-15).
- [x] `requirements.txt` pins dependency versions, including pandas, NumPy, scikit-learn, SciPy, statsmodels, PyArrow, VADER, NRCLex, textstat, and lexicalrichness.
- [ ] Clean installation from `requirements.txt` is not verified. The file is UTF-16 encoded in this checkout; test compatibility with pip or provide a UTF-8 requirements file before using the README's install instruction.
- [x] The project config sets random seed 42 and nominal test size 0.20 in [`src/config.py`](../src/config.py).
- [ ] Hardware, operating-system matrix, exact package lock provenance, and deterministic cross-platform behavior are not documented.

## Data Access and Preparation

- [x] Local raw CSV record counts and timestamp ranges were measured on 2026-10-15: 10,234 Reddit rows and 12,000 X rows, covering 2023-10-07 through 2023-10-30.
- [x] Local processed Parquet counts were measured: 9,409 Reddit, 11,733 X, and 9,000 per platform in the feature-engineered comparison files.
- [ ] Dataset provider IDs, URLs, versions, retrieval dates, licenses, and collection queries are unknown. The README's Pushshift/Hugging Face claims are not corroborated by source metadata.
- [ ] Row-level exclusions, sampling procedure, duplicate treatment, and cleaning decisions are not fully documented. The configured 1,440-hour window conflicts with the comment calling it 30 days (1,440 hours is 60 days).
- [ ] Raw data are ignored by Git and are not available to another user from this repository alone. Obtain authorized access and document secure acquisition without committing restricted records.

## Execution and Evaluation

- [x] Notebook files `01_data_preprocessing.ipynb` through `05_hypothesis_validation.ipynb` exist in the checkout; their order is preprocessing, feature engineering, EDA, hypothesis validation, then computational modeling.
- [x] Feature methods are implemented in [`src/features`](../src/features); model experiment code is in [`notebooks/04_computational_model.ipynb`](../notebooks/04_computational_model.ipynb), and hypothesis notebook code is in [`notebooks/05_hypothesis_validation.ipynb`](../notebooks/05_hypothesis_validation.ipynb).
- [x] The stored feature Parquet tables were loaded successfully; selected descriptive values for readability, rigor, link rates, and sentiment were recomputed directly from them on 2026-10-15.
- [ ] The full notebooks have not been run from a clean kernel in this verification. Their saved outputs are not proof that the current source recreates them.
- [ ] `python main.py` does not currently run: it fails with `ModuleNotFoundError` for `src.hypothesis_validation`.
- [ ] `python -m pytest -q` cannot verify behavior: pytest reports no tests ran, and `tests/` contains only `.gitkeep`.
- [ ] Saved model and hypothesis metrics have not been regenerated. Model accuracy and evidentiary/temporal summaries disagree across saved artifacts; see [`model_card.md`](model_card.md) and [`failure_log.md`](failure_log.md).
- [ ] The Random Forest preprocessing fills missing features using full-data means before the split; evaluation should be rerun with imputation fitted within training folds before claiming a leakage-safe holdout estimate.

## Regenerating Outputs: Current Constraints

The notebooks indicate that generated tables and figures are written under `results/`, and the feature workflow writes Parquet files under `data/processed/`. Those outputs are ignored by Git. The README's `pip install -r requirements.txt` instruction is not verified, the source dataset acquisition path is undocumented, and the current top-level `main.py` import fails. Therefore no complete end-to-end command sequence can responsibly be given as verified.

After resolving access and source issues, a reproducible run should record: dataset checksums and versions; exact notebook order and kernel; package installation log; sampling and exclusion counts; random seed; frozen train/test indices; feature columns; model parameters; and checksums/timestamps for regenerated tables, figures, and model files. Do not overwrite the current local outputs until they have been backed up and the researcher has approved regeneration.

## Verification Levels

- **Instructions documented:** Partial; README describes installation and project outline but not a complete run.
- **Code inspected:** Yes for configuration, feature modules, notebooks, and entry point.
- **Selected data artifacts checked:** Yes; local row counts, date coverage, Parquet shapes, and selected descriptive values were recomputed.
- **Code execution tested:** `main.py` failed at import; pytest found no tests.
- **Results regenerated:** No.
- **Results independently verified:** Only selected descriptive statistics calculated from the current feature Parquet files; inferential tests and predictive metrics were not independently rerun.
