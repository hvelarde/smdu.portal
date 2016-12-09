# -*- coding: utf-8 -*-
from plone import api
from smdu.portal.testing import INTEGRATION_TESTING

import unittest


class SiteSettingsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.languages = self.portal['portal_languages']

    def test_use_combined_language_codes(self):
        self.assertEqual(self.languages.use_combined_language_codes, 1)

    # XXX: https://github.com/gforcada/flake8-plone-api/issues/17
    def test_pt_br_is_default_language(self):  # noqa: P001
        self.assertEqual(api.portal.get_default_language(), 'pt-br')  # noqa: P001
