"""Shared metadata for static pages; no runtime service required."""
import html
import json
import os
from urllib.parse import urlsplit


def site_origin():
    origin = os.getenv('SITE_ORIGIN')
    if not origin and os.getenv('VERCEL_PROJECT_PRODUCTION_URL'):
        origin = 'https://' + os.environ['VERCEL_PROJECT_PRODUCTION_URL']
    if not origin and os.getenv('VERCEL'):
        raise ValueError('Set SITE_ORIGIN to the public HTTPS origin before deploying.')
    origin = (origin or 'https://findoldstreet.amusingdelta5.chatgpt.site').rstrip('/')
    parsed = urlsplit(origin)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.path or parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError('SITE_ORIGIN must be an HTTPS origin without a path, query, or credentials.')
    return origin


def metadata(origin, lang, suffix, title, description, record=None, noindex=False):
    url = f'{origin}/{lang}/{suffix}'
    noindex = noindex or os.getenv('VERCEL_ENV') in ('preview', 'development')
    esc = lambda value: html.escape(str(value), quote=True)
    tags = [f'<meta name="robots" content="{"noindex, follow" if noindex else "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1"}">']
    for key, value in {'og:type': 'website', 'og:site_name': 'FindOldStreet', 'og:title': title + ' | FindOldStreet', 'og:description': description, 'og:url': url}.items():
        tags.append(f'<meta property="{key}" content="{esc(value)}">')
    for key, value in {'twitter:card': 'summary', 'twitter:title': title + ' | FindOldStreet', 'twitter:description': description}.items():
        tags.append(f'<meta name="{key}" content="{esc(value)}">')
    if noindex:
        return ''.join(tags)
    website = {'@type': 'WebSite', '@id': origin + '/#website', 'name': 'FindOldStreet', 'url': origin + '/en/'}
    page = {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': title, 'description': description, 'inLanguage': lang, 'isPartOf': {'@id': website['@id']}}
    graph = [website, page]
    if record:
        # A documented name mapping does not establish current geometry or house numbers.
        page['about'] = {'@type': 'Place', 'name': record['currentName'], 'alternateName': list(dict.fromkeys([record['formerName'], *record.get('aliases', [])])), 'address': {'@type': 'PostalAddress', 'addressLocality': record['city'], 'addressCountry': record['country']}}
        page['citation'] = list(dict.fromkeys(s['url'] for s in record['sources']))
    if suffix == 'coverage/':
        page['mainEntity'] = {'@type': 'Dataset', 'name': 'FindOldStreet documented street renamings', 'description': description, 'url': url, 'distribution': {'@type': 'DataDownload', 'encodingFormat': 'application/json', 'contentUrl': origin + '/records.json'}}
    encoded = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c')
    tags.append(f'<script type="application/ld+json">{encoded}</script>')
    return ''.join(tags)
