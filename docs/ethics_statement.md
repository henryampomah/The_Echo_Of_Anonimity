# Ethics Statement

**Status:** Ethical assessment based on repository evidence; institutional status requires confirmation  
**Last updated:** 2026-10-15

## Purpose and Scope

This project explores political discourse about the Israel-Hamas war in locally held Reddit-comment and X-post data. It computes aggregate lexical, link/evidentiary-proxy, sentiment, engagement, and temporal features. The analysis involves politically sensitive content, conflict-related speech, and user/account metadata. This statement documents repository-visible practices and outstanding questions; it is not legal advice or evidence of ethics approval.

## Data, Privacy, and Permissions

The README claims Pushshift as the Reddit source and Hugging Face datasets as the X source, but the actual dataset identifiers, versions, retrieval dates, collection method, terms, and licenses are not supplied. The raw files contain usernames or author names, timestamps, post/comment text, community/account fields, and engagement metadata. Their presence on a local machine does not establish permission to collect, retain, or redistribute them.

The raw, processed, and result data files are excluded by `.gitignore` in this checkout. No explicit access-control, encryption, retention, deletion, or de-identification procedure is documented. The researcher should keep the raw data access-restricted, minimize copies, avoid adding user-level records to public releases, and confirm provider terms before any sharing.

Public posts can still carry contextual privacy expectations. Searchable quotations, usernames, profile URLs, and combinations of timestamps/community metadata can expose individuals, including people discussing traumatic events or belonging to vulnerable groups. Documentation and publication should use aggregate statistics and paraphrase where possible; avoid verbatim searchable text unless justified, approved, and permitted.

## Anonymity, Fairness, and Interpretation

Reddit and X have different account, community, visibility, and interaction structures. Reddit participation is not necessarily anonymous, and X pseudo-identifiers do not prove that a user is publicly identifiable. Neither platform identity nor a username field measures a participant's perceived or actual anonymity. The project does not manipulate or directly measure anonymity, threading, recommendation exposure, or visibility curation. Observed platform differences cannot be attributed to anonymity or platform design without a suitable research design and controls.

The local samples cover one event and are unequal in raw size, record type, metadata, and sampling history; only 9,000 rows per platform appear in feature tables. There is no evidence that they represent platform populations, political groups, languages, or the full event discourse. English-language filtering may exclude multilingual and code-switched voices. Subreddit selection, platform-specific data availability, engagement differences, and missing X link fields may bias comparisons.

Readability scores are proxies, not direct measures of intelligence or quality. Heuristic link and word-list scores do not establish truth, source reliability in context, or good-faith reasoning. Sentiment and emotion outputs are lexicon/model estimates and must not be presented as verified human feelings, beliefs, or intentions. The classifier predicts a platform label from mixed linguistic and non-linguistic features; it must not be used to profile people or infer political identity.

## Oversight, Consent, and Publication

No ethics-board approval, consent process, exemption determination, or institutional review decision is documented. Whether secondary analysis of these data requires review depends on the institution, jurisdiction, source terms, identifiability, and intended publication. The researcher should ask their supervisor or research ethics committee whether review or an exemption determination is required before further analysis or publication. Do not claim approval or consent without documentary evidence.

Before release, review raw and derived artifacts for identifiers, sensitive quotations, and re-identification risk; confirm data-provider terms; publish only necessary aggregate outputs; document the limitations above; and provide a route for questions or takedown requests where appropriate. Retention and deletion schedules remain to be established with the institution and data provider.

## Outstanding Ethical Risks

The unresolved provenance and license, user-level fields, conflict-related content, absent documented ethics review, and the possibility of overstating platform/anonymity causality are material risks. The project should not be represented as ethically approved or as anonymized until those facts and controls are confirmed.
