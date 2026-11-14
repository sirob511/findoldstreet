# FindOldStreet

Static, multilingual street-rename lookup with a repeatable, source-backed import pipeline. Source is in `src/`, adapters in `scripts/`, audit evidence in `data/sources/`. See [COVERAGE.md](COVERAGE.md) for actual locality counts, source URLs and limitations.

## Run

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm ci
.venv/bin/python scripts/import_data.py
npm run build
python3 scripts/report.py
npm run preview
```

Open http://localhost:4173. Building uses Python's standard library; importing needs the Python dependencies. The app has no runtime API keys, database or paid service dependencies. Search is local to the browser, while every lookup and populated locality has static HTML.

## Refresh imports

`fetch_sources.py` runs six country downloads concurrently. `expand_sources.py`, `more_sources.py`, `final_sources.py`, and `saigon_sources.py` preserve further discovery downloads and their failures. Network refresh is separate from the deterministic importer so a temporarily blocked portal does not erase audited evidence. Browser-only captures have provenance and row locators. Never promote an unchecked new source or OCR output automatically. Review changed evidence and diffs before rebuilding.

`import_data.py` runs the six country adapters concurrently, uses deterministic street/segment identifiers, reconciles documented Warsaw reversals, keeps same-name streets separated by locality/district, and holds ambiguous combined objects for review. `currentStatusVerified` is separate from `status`: source-supported renames are not claimed to have current GIS or national-register verification. Unknown effective dates stay null; decision/ceremony dates are separate. No coordinates or house-number carryover are fabricated.

Source spelling and generated transliterations remain separate. Source documents are retained for local audit; only factual mappings, source links and the report are published. Recorded reuse terms are not a blanket licence determination for entire source documents.

## Validate

```sh
npm test
python3 tests/seo.py
# with the preview server running:
node tests/browser.mjs
```

Tests use real records for exact/partial/transliterated queries, disambiguation, repeated renames, reversals and partial streets. Browser checks cover desktop search → detail → locale switching and mobile overflow in all 11 languages.

## Hosting and indexing

For Vercel, the checked-in `vercel.json` selects the **Other** framework preset,
runs the Python static-page generator, and publishes only `dist/`. Configuration
is provided for either the repository root or `site/` as the Vercel Root Directory.
No Python server entrypoint is needed. Dependency installation is skipped because
the build uses only Python's standard library and the committed data. Set
`SITE_ORIGIN` to your public site's HTTPS origin before deploying so canonical
URLs and sitemaps point to the correct domain.

`.openai/hosting.json` identifies the private Sites deployment; `dist/` is the static artifact. `SITE_ORIGIN` controls absolute canonicals, reciprocal hreflang and locale sitemaps (defaults to the actual Sites origin). It must be changed and rebuilt when deploying under FindOldStreet.com. DNS/custom-domain setup and public indexing are not completed: private hosting cannot be crawled publicly.

Stable routes are `/{locale}/street/{id}/`. Every alias searches the same record and links to that route. City routes use stable hashes of source locality names. Source spellings are never silently translated. District labels refer to the cited decision's geography; newer administrative boundary changes may not be reconciled.

This is an initial release, not exhaustive worldwide or national coverage. Maps open name/locality searches on OpenStreetMap; verified geometry, OSM object history, general OCR and municipal-register reconciliation remain unfinished. The coverage report lists these gaps explicitly. Translations need native-speaker editorial review.
