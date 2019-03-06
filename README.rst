Git Version
===========

A simple tool for extracting version information from git tags and formatting
it with optional post-release commit info.

The post-release commit info can tell you if there have been additional commits
beyond the revision tagged with the release version.  For example,
an output of ``1.0.0+git-1-123abcd`` would indicate that the version in use is
one commit after the 1.0.0 release, with the current commit having a SHA of
``123abcd``.

Installation
------------

Install from PyPI::

    pip install git-version


Usage
-----

Full usage::

    git-version [-h] [--format {long,short,default,json}] [path]

The ``path`` can be omitted and defaults to the current directory.

There are several different formats which can be used:

  * ``long`` Always include the git revision info.
  * ``short`` Never include the git revision info.
  * ``default`` Hide the git revision info unless the current release is a
    pre-release or there are additional commits after the release.
  * ``json`` Output JSON data describing the version, in the form:

.. code-block:: json

   {
     'version': '{release_version}',
     'git': '+git-{gitn}-{gitsha}',
     'gitn': '{gitn}',
     'gitsha': '{gitsha}',
     'pre_release': true // if gitn > 0 else false
   }
