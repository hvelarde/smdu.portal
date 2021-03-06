# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0'
description = 'SMDU Portal'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='smdu.portal',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='smdu',
    author='Héctor Velarde',
    author_email='hector.velarde@gmail.com',
    url='https://github.com/hvelarde/smdu.portal',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['smdu'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.cover',
        'collective.feedaggregator',
        'collective.fingerpointing',
        'collective.lazysizes',
        'collective.nitf',
        'collective.revisionmanager',
        'collective.themecustomizer',
        'collective.upload',
        'eea.facetednavigation',
        'pas.plugins.ldap',
        'plone.app.caching',
        'plone.app.contenttypes',
        'plone.app.theming',
        'smdu.identidadevisual',
        'plone.resource',
        'Products.GenericSetup',
        'Products.PloneFormGen',
        'Products.PloneKeywordManager',
        'Products.RedirectionTool',
        'sc.embedder',
        'sc.photogallery',
        'sc.social.like',
        'setuptools',
        'webcouturier.dropdownmenu',
        'z3c.jbot',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.browserlayer',
            'plone.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
