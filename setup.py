#!/usr/bin/env python
"""
sentry-auth-github
==================

:copyright: (c) 2016 Functional Software, Inc
"""
from setuptools import setup, find_packages


install_requires = [
    'sentry>=7.0.0',
    'requests>=2.18.0'
]

tests_require = [
    'mock',
    'flake8>=2.0,<2.1',
]

setup(
    name='sentry-auth-thalia',
    version='1.0.0',
    author='Thalia Technicie',
    author_email='technicie@thalia.nu',
    description='Thalia authentication provider for Sentry',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_thalia = sentry_auth_thalia',
        ],
    },
)
