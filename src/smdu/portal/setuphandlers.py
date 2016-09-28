# -*- coding: utf-8 -*-
from plone import api
from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonInstallableProducts
from zope.interface import implementer


@implementer(INonInstallableProducts)
class NonInstallableProducts(object):

    def getNonInstallableProducts(self):
        return [
            'pas.plugins.ldap',
            'yafowil.plone',
        ]


@implementer(INonInstallable)
class NonInstallable(object):

    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
        return [
            u'collective.cover:default',
            u'collective.feedaggregator:default',
            u'collective.fingerpointing:default',
            u'collective.js.cycle2:default',
            u'collective.js.galleria:default',
            u'collective.js.jqueryui:default',
            u'collective.lazysizes:default',
            u'collective.nitf:default',
            u'collective.themecustomizer:default',
            u'collective.themecustomizer:uninstall',
            u'collective.upload:default',
            u'eea.facetednavigation:default',
            u'eea.facetednavigation:universal',
            u'eea.jquery:01-jquery',
            u'eea.jquery:02-ui',
            u'eea.jquery:03-ajaxfileupload',
            u'eea.jquery:04-bbq',
            u'eea.jquery:05-cookie',
            u'eea.jquery:06-fancybox',
            u'eea.jquery:07-flashembed',
            u'eea.jquery:08-galleryview',
            u'eea.jquery:09-jqzoom',
            u'eea.jquery:10-jstree',
            u'eea.jquery:11-reflection',
            u'eea.jquery:12-select2uislider',
            u'eea.jquery:13-splitter',
            u'eea.jquery:14-tagcloud',
            u'eea.jquery:15-tools',
            u'eea.jquery:16-tokeninput',
            u'eea.jquery:17-jqgrid',
            u'eea.jquery:18-slickgrid',
            u'eea.jquery:19-colorpicker',
            u'eea.jquery:20-annotator',
            u'eea.jquery:21-serialscroll',
            u'eea.jquery:22-masonry',
            u'eea.jquery:23-select2',
            u'eea.jquery:24-timeoutdialog',
            u'eea.jquery:25-rememberstate',
            u'eea.jquery:26-knob',
            u'eea.jquery:27-dracula',
            u'pas.plugins.ldap.plonecontrolpanel:default',
            u'pas.plugins.ldap.plonecontrolpanel:yafowil',
            u'plone.app.blocks:default',
            u'plone.app.contenttypes:plone-content',
            u'plone.app.dexterity:default',
            u'plone.app.drafts:default',
            u'plone.app.event.at:default',
            u'plone.app.event:default',
            u'plone.app.iterate:plone.app.iterate',
            u'plone.app.referenceablebehavior:default',
            u'plone.app.relationfield:default',
            u'plone.app.theming:default',
            u'plone.app.tiles:default',
            u'plone.app.versioningbehavior:default',
            u'plone.formwidget.autocomplete:default',
            u'plone.formwidget.contenttree:default',
            u'plone.formwidget.querystring:default',
            u'plone.formwidget.recurrence:default',
            u'plone.session:default',
            u'Products.CMFPlacefulWorkflow:base',
            u'Products.PloneFormGen:default',
            u'Products.PloneKeywordManager:default',
            u'Products.PloneKeywordManager:uninstall',
            u'sc.embedder:default',
            u'sc.photogallery:default',
            u'sc.social.like:default',
            u'webcouturier.dropdownmenu:default',
            u'yafowil.plone:default',
        ]

def disable_news_items():
    """We are using collective.nitf as preferred news content type."""
    types_tool = api.portal.get_tool('portal_types')
    types_tool['News Item'].global_allow = False


def post_install(context):
    """Post install script."""
    disable_news_items()
