Thalia Auth for Sentry
======================

An SSO provider for Sentry which enables authentication via `thalia.nu`_.

Install
-------

::

   $ pip install -e .

Setup
-----

Add the following variables to ``sentry.conf.py``

::

   THALIA_API_URL = ""
   THALIA_API_SECRET = ""

.. _thalia.nu: https://thalia.nu
