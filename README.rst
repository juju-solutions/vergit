vergit
======

A simple tool for extracting version information from git tags and formatting
it with optional post-release commit info.

Installation
------------

Install from PyPI::

    pip install vergit


Usage
-----

Full usage::

    vergit [-h] [--format {long,short,default,json}] [path]

The ``path`` can be omitted and defaults to the current directory.

There are several different formats which can be used:

* **long** Always include the git revision info.  For example,
  ``1.0.0+git-1-123abcd`` means you are currently on commit ``123abcd``
  which is one commit newer than the 1.0.0 release.
* **short** Never include the git revision info, only the release version.
  For example, ``1.0.0`` or ``1.0.0rc1``.
* **default** Uses the long format if on a pre-release or there are commits
  after the release, or the short format if exactly on a release.  For example,
  ``1.0.0``, ``1.0.0rc1+git-0-123abcd``, or ``1.0.0+git-1-123abcd``.
* **json** Output JSON data describing the version.  E.g.:

.. code-block:: json

   {
     "version": "1.0.0",
     "git": "+git-0-123abcd",
     "gitn": "0",
     "gitsha": "123abcd",
     "pre_release": false
   }
