# -*- coding: utf-8 -*-
from smdu.portal.config import PROJECTNAME
from smdu.portal.interfaces import IBrowserLayer
from smdu.portal.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers

import unittest

DEPENDENCIES = (
    'collective.cover',
    'collective.feedaggregator',
    'collective.fingerpointing',
    'collective.lazysizes',
    'collective.nitf',
    'collective.themecustomizer',
    'collective.upload',
    # 'plone.app.contenttypes',  # FIXME: add-on reported as not installed
    'plone.app.theming',
    'PloneFormGen',
    'PloneKeywordManager',
    'sc.embedder',
    'sc.photogallery',
    'sc.social.like',
    'webcouturier.dropdownmenu',
)


class InstallTestCase(unittest.TestCase):

    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_dependencies_installed(self):
        expected = set(DEPENDENCIES)
        installed = self.qi.listInstalledProducts(showHidden=True)
        installed = set([product['id'] for product in installed])
        result = sorted(expected - installed)
        self.assertEqual(result, [], 'Not installed: ' + ', '.join(result))

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())
