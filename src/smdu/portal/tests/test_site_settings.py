# -*- coding: utf-8 -*-
from smdu.portal.testing import INTEGRATION_TESTING

import unittest


class SiteSettingsTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.languages = self.portal['portal_languages']

    def test_portal_title(self):
        self.assertEqual(self.portal.title, 'SMDU Portal')

    def test_use_combined_language_codes(self):
        self.assertEqual(self.languages.use_combined_language_codes, 1)

    def test_pt_br_is_default_language(self):
        self.assertEqual(self.languages.getDefaultLanguage(), 'pt-br')
