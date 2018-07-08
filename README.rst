GitHub Auth for Thalia
======================

An SSO provider for Sentry which enables authentication via www.thalia.nu.

Install
-------

::

    $ pip install https://gitlab.science.ru.nl/thalia/sentry-auth-thalia/repository/master/archive.zip

Setup
-----

Create a new application under your organization in GitHub. Enter the **Authorization
callback URL** as the prefix to your Sentry installation:

::

    https://example.sentry.com


Once done, grab your API key and drop it in your ``sentry.conf.py``:

.. code-block:: python

    THALIA_API_DOMAIN = ""

    THALIA_API_SECRET = ""
