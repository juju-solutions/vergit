vergit
======

A simple tool for extracting version information from git tags and formatting
it with optional post-release commit info.

Version tags can optionally use a ``v`` prefix, and can include pre-release
versions.

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

* **long** Always include the git revision info.
  which is one commit newer than the 1.0.0 release.
* **short** Never include the git revision info, only the release version.
* **default** Uses the long format if on a pre-release or there are commits
  after the release, otherwise the short format.
* **json** Output JSON data describing the version.


Examples
--------

If the current commit is tagged with ``v1.0.0``::

    $ vergit
    1.0.0

    $ vergit --format=short
    1.0.0

    $ vergit --format=long
    1.0.0+git-0-123abcd

    $ vergit --format=json
    {"version": "1.0.0", "git": "+git-0-123abcd", "gitn": "0", "gitsha": "123abcd", "pre_release": false}

If the commit before the current is tagged with ``1.0.0``::

    $ vergit
    1.0.0+git-1-123abcd

    $ vergit --format=short
    1.0.0

    $ vergit --format=long
    1.0.0+git-0-123abcd

    $ vergit --format=json
    {"version": "1.0.0", "git": "+git-1-123abcd", "gitn": "1", "gitsha": "123abcd", "pre_release": false}

If the current commit is tagged with ``v1.0.0rc1``::

    $ vergit
    1.0.0rc1+git-0-123abcd

    $ vergit --format=short
    1.0.0rc1

    $ vergit --format=long
    1.0.0rc1+git-0-123abcd

    $ vergit --format=json
    {"version": "1.0.0rc1", "git": "+git-0-123abcd", "gitn": "0", "gitsha": "123abcd", "pre_release": true}
