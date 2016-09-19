# -*- coding: utf-8 -*-
from plone import api


def disable_news_items():
    """We are using collective.nitf as preferred news content type."""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['News Item'].global_allow = False


def post_install(context):
    """Post install script."""
    disable_news_items()
