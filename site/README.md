# FindOldStreet

Static, multilingual street, city and country rename lookup with a repeatable, source-backed import pipeline. Source is in `src/`, adapters in `scripts/`, audit evidence in `data/sources/`. See [COVERAGE.md](COVERAGE.md) for actual locality counts, source URLs and limitations.

## Run

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
npm ci
.venv/bin/python scripts/import_data.py
python3 scripts/audit_sources.py
python3 scripts/report.py
npm run build
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
python3 tests/reviewed_data.py
python3 tests/expanded_data.py
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

## Search and AI discoverability

Every published street and locality has crawlable HTML, canonical URLs and
reciprocal language links. Pages include descriptive metadata, social preview
metadata and JSON-LD; street metadata cites original evidence. The coverage page
identifies the downloadable dataset without claiming an unverified reuse licence.
`robots.txt` permits crawlers, including AI search crawlers, and advertises the
sitemap. `llms.txt` is an optional navigation guide, not an indexing requirement
or a guarantee that an AI service will cite the site.

Set `SITE_ORIGIN=https://your-public-domain` in production. On Vercel, if omitted,
`VERCEL_PROJECT_PRODUCTION_URL` supplies the production origin. A Vercel build
without either value fails rather than publishing canonicals for the private
Sites host. Local builds retain the original Sites default. Preview builds use
`noindex`; the root URL permanently redirects to `/en/` on Vercel.

After deploying, ensure the production site is publicly accessible without login
or bot challenges. Verify domain ownership in Google Search Console and Bing
Webmaster Tools and submit `/sitemap.xml`. These account steps are separate from
repository configuration. Indexing, ranking and AI citations are not guaranteed.

Verification:

```sh
python3 tests/metadata.py
npm run build
python3 tests/seo.py
```

### Reviewed municipal expansion

`data/sources/reviewed-additions.json` contains individually reviewed mappings
from the Kharkiv regional order, Łódź municipal naming dictionary, Cape Town
language guide, Tshwane tourism map and Kolkata municipal newsletter. Import
these with `scripts/import_data.py`; the importer replays them deterministically.
The expansion and Łódź manifests retain retrieval timestamps and SHA-256 hashes.
`lodz-reviewed-index.json` records the dictionary anchors used during review.
Archived documents stay out of the generated public site.

Keep uncertain spellings, partial-road boundaries and conflicting evidence in
`review` status. Historical source support does not establish the latest live
street-register name, coordinates or house-number correspondence. Year-only
sources retain year precision; announcement dates are not inferred effective dates.

Run `python3 tests/reviewed_data.py` after importing. The research backlog in
`data/research-backlog.json` records promising sources and unresolved issues.

### Unified place lookup

The homepage uses one field for a former street, city or country name, including
an optional locality in the same query. Results remain hidden until a query or
country browse is selected. Ambiguous street matches expose city/district
choices; answer rows link to history, source evidence and map searches.

`data/places.json` holds the initial, manually reviewed city and country
renamings, separately from the municipal street imports. The build and coverage
report include these records without presenting them as street records. New
city/country detail routes use `/{locale}/place/{id}/`; existing street URLs stay
stable. All detail pages have a search form for the next lookup. Effective dates
remain unknown when the cited source only confirms a decision or signature.

### City, country and further street coverage

`coverage-additions.json` contains reviewed Lviv appendix 2, Shymkent and further
Łódź street mappings. `places-reviewed.json` supplies city/country mappings to
`import_places.py`, called by the main importer; `places-seed.json` preserves
the original public routes. The coverage-expansion manifest records successful
captures and failed retrievals. `lodz-expansion-review.json` records candidate
decisions and `lodz-current-checks.json` records current-name comparison.

Run `python3 scripts/audit_sources.py` to inventory every repository source
manifest and connect its URLs to published and review records. The resulting
`data/source-audit.json` distinguishes imported evidence, background material,
failed attempts and leads still requiring row-level review. Then regenerate
the report before building. This audit is not a worldwide source census.

Country short-name changes, historical territories and boundary limitations
have notes on their detail pages. New country labels use English names where
localized labels are not yet reviewed. Source-supported historical mappings
do not imply that historical and present boundaries are identical.
