# Verification

The tested flow is search input → downloaded static dataset → name/locality matching → stable record page → evidence and map-search links.

- Eight automated tests pass using real imported records: all six countries, accentless search, Ukrainian transliteration, city aliases, partial addresses, Warsaw reversals, repeated renames, duplicate old names across Almaty districts, partial renames, review exclusion, unique IDs and complete locale keys.
- Browser test at desktop width: Smith Street returns Anton Lembede; opening the result shows its history; switching to Ukrainian preserves the record route. No JavaScript page errors.
- Browser overflow checks pass at 390 px in all 11 locales. Desktop and mobile screenshots were inspected.
- Self-canonicals and reciprocal hreflang pass in every locale. Every URL in every locale sitemap resolves to a generated file.
- Review records have no generated detail pages. The build replaces its output directory so stale files cannot escape review exclusions.
- Re-importing all six countries against the captured evidence is byte-for-byte idempotent.
- Preview server serves HTTP 200. Data and translation fetches render working search results.

Limits: external map searches are not geocoding verification; current national registers, OSM history and house numbers are not verified. No native-speaker translation review. Public indexing and FindOldStreet.com DNS are not configured. Country and locality coverage is incomplete; consult COVERAGE.md.
