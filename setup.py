#!/usr/bin/env python
"""
sentry-auth-thalia
==================

:copyright: (c) 2016 Functional Software, Inc
"""
from setuptools import setup

setup(
    name='sentry-auth-thalia',
    version='1.0.0',
    author='Thalia Technicie',
    author_email='technicie@thalia.nu',
    description='Thalia authentication provider for Sentry',
    long_description=__doc__,
    packages=['sentry_auth_thalia'],
    zip_safe=False,
    install_requires=[
        'requests>=2.18.0'
        ],
    tests_require=['flake8'],
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'auth_thalia = sentry_auth_thalia',
        ],
    },
)
