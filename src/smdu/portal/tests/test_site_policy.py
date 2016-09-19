# -*- coding: utf-8 -*-
from smdu.portal.testing import INTEGRATION_TESTING

import unittest


class SitePolicyTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_can_not_add_news_items(self):
        types_tool = self.portal['portal_types']
        self.assertFalse(types_tool['News Item'].global_allow)
