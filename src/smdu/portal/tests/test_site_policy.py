# -*- coding: utf-8 -*-
from smdu.portal.testing import INTEGRATION_TESTING
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class SitePolicyTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

        vocab = getUtility(
            IVocabularyFactory, 'collective.cover.EnabledTiles')
        self.enabled_tiles = vocab(self.portal)

    def test_can_not_add_news_items(self):
        types_tool = self.portal['portal_types']
        self.assertFalse(types_tool['News Item'].global_allow)

    def test_embedder_tile_enabled(self):
        self.assertIn(u'sc.embedder', self.enabled_tiles)

    def test_feed_aggregator_tile_enabled(self):
        self.assertIn(u'collective.feedaggregator', self.enabled_tiles)

    def test_nitf_tile_enabled(self):
        self.assertIn(u'collective.nitf', self.enabled_tiles)

    def test_photo_gallery_tile_enabled(self):
        self.assertIn(u'sc.photogallery', self.enabled_tiles)
