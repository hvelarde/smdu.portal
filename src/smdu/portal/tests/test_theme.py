# -*- coding: utf-8 -*-
from smdu.portal.testing import INTEGRATION_TESTING

import unittest


class ThemeTestCase(unittest.TestCase):

    """Ensure theme is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_available_themes(self):
        from plone.app.theming.utils import getAvailableThemes
        themes = getAvailableThemes()
        self.assertEqual(len(themes), 5)

    def test_theme_enabled(self):
        from plone.app.theming.utils import isThemeEnabled
        self.assertTrue(isThemeEnabled(self.request))

    def test_current_theme(self):
        from plone.app.theming.utils import getCurrentTheme
        theme = getCurrentTheme()
        self.assertEqual(theme, u'Default')

    def test_default_theme(self):
        from plone.app.theming.utils import getTheme
        theme = getTheme('Default')
        self.assertIsNotNone(theme)
        self.assertEqual(theme.title, 'Tema Padrão SMDU')
        self.assertEqual(
            theme.description,
            'Tema Diazo padrão para uso no projeto SMDU Portal.',
        )
        self.assertEqual(theme.absolutePrefix, '/++theme++Default')
        self.assertEqual(theme.rules, '/++theme++Default/rules.xml')
        self.assertEqual(theme.doctype, '<!DOCTYPE html>')
