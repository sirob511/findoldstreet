import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from seo import site_origin, metadata

class MetadataTests(unittest.TestCase):
    def test_custom_origin_and_vercel_fallback(self):
        with patch.dict(os.environ, {'SITE_ORIGIN': 'https://example.org/', 'VERCEL_PROJECT_PRODUCTION_URL': 'project.vercel.app'}, clear=True):
            self.assertEqual(site_origin(), 'https://example.org')
        with patch.dict(os.environ, {'VERCEL': '1', 'VERCEL_PROJECT_PRODUCTION_URL': 'project.vercel.app'}, clear=True):
            self.assertEqual(site_origin(), 'https://project.vercel.app')
    def test_invalid_or_missing_deployment_origin(self):
        for value in ['http://example.org', 'https://example.org/path', 'https://user:pass@example.org', 'https://example.org?q=x']:
            with patch.dict(os.environ, {'SITE_ORIGIN': value}, clear=True), self.assertRaises(ValueError):
                site_origin()
        with patch.dict(os.environ, {'VERCEL': '1'}, clear=True), self.assertRaises(ValueError):
            site_origin()
    def test_preview_and_error_pages_are_not_indexable(self):
        with patch.dict(os.environ, {'VERCEL_ENV': 'preview'}, clear=True):
            result = metadata('https://example.org', 'en', '', 'Title', 'Description')
            self.assertIn('noindex, follow', result)
            self.assertNotIn('application/ld+json', result)
        self.assertIn('noindex, follow', metadata('https://example.org', 'en', '', '404', '', noindex=True))
    def test_jsonld_escaping_and_evidence(self):
        record = {'currentName': '</script><script>bad', 'formerName': 'Old', 'city': 'City', 'country': 'ZA', 'sources': [{'url': 'https://example.org/evidence'}]}
        with patch.dict(os.environ, {}, clear=True):
            result = metadata('https://example.org', 'en', 'street/id/', 'Title', 'Description', record)
        payload = result.split('<script type="application/ld+json">')[1].split('</script>')[0]
        page = json.loads(payload)['@graph'][1]
        self.assertEqual(page['citation'], ['https://example.org/evidence'])
        self.assertEqual(page['about']['name'], record['currentName'])
        self.assertNotIn('<script>bad', result)
        self.assertNotIn('geo', page['about'])

unittest.main()
