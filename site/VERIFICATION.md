# Verification

The tested flow is one-box search → downloaded static dataset → name/locality matching → stable detail page → source and map-search links.

- 14 search regression tests cover streets, cities, countries, transliteration, locality aliases, numbered streets, reversals, partial renames, disambiguation and record identifiers.
- All 3,811 international additions are checked against captured source fields and hashes. Checks include current-name/type matches for Wrocław, road-name matches for Vilnius, abolished-street exclusions for Brno, PDF table-cell evidence for Chișinău and EKI fields for Tallinn.
- Final review withheld 59 Brno compound, alternate-label-list or isolated-house entries. The retained Brno pass contains 510 mappings.
- Existing curated, expanded and postal-data checks pass, including all 4,206 postal street mappings and 13 city additions from the previous five passes. All 5,906 pre-expansion records, including review rows, remain unchanged.
- All eight data files replay deterministically from captured evidence without network requests; the published JSON matches the verified source records.
- Browser checks cover searches and source links for every new country/city group, existing postal searches, country and city details, legacy links, locale switching, empty/reset behavior and mobile overflow in all 11 locales.
- Metadata tests, reciprocal hreflang, canonical links and every locale sitemap target pass. Withheld entries have no published detail pages.
- The retained dataset contains 9,675 records across 33 countries. Unknown effective dates remain null; decision dates are kept separately.

Limits: inventory checks establish name existence, not historical boundary continuity or current GIS identity. The Chișinău guide is from 2017 and the Tallinn snapshot from 2018; later changes are not comprehensively reconciled. Maps remain name searches and house numbers are unverified. Translation review, public indexing and custom-domain configuration remain outside these checks. See [COVERAGE.md](COVERAGE.md) for source-specific gaps.
