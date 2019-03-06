#!/usr/bin/env python
#
# Copyright 2019 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3 (see the file LICENSE).

import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fh:
    readme = fh.read()

setup(
    name='git_version',
    version='1.0.0',
    packages=[
        'git_version',
    ],
    install_requires=[
        'setuptools',
    ],
    include_package_data=True,
    maintainer='Cory Johns',
    maintainer_email='johnsca@gmail.com',
    description=('Tool for getting version info from git history'),
    long_description=readme,
    license='GPL v3',
    url='https://github.com/juju-solutions/git-version',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'git-version = git_version:main',
        ],
    },
)
