#!/usr/bin/env python
#
# Copyright 2019 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3 (see the file LICENSE).

import json
import os
import subprocess
import sys
from setuptools import setup

curdir = os.path.dirname(__file__)
version_cache = os.path.join(curdir, 'vergit', 'VERSION')
version_script = os.path.join(curdir, 'vergit', '__init__.py')
version_raw = subprocess.check_output([sys.executable, version_script,
                                       '--format=json']).strip()
if sys.version_info >= (3, 0):
    version_raw = version_raw.decode('UTF-8')
version = json.loads(version_raw)['version']
if version == 'unknown':
    # during install; use cached VERSION
    with open(version_cache, 'r') as fh:
        version_raw = fh.read()
    version = json.loads(version_raw)['version']
else:
    # during build; update cached VERSION
    with open(version_cache, 'w') as fh:
        fh.write(version_raw)

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fh:
    readme = fh.read()

setup(
    name='vergit',
    version=version,
    packages=[
        'vergit',
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
    url='https://github.com/juju-solutions/vergit',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
    ],
    entry_points={
        'console_scripts': [
            'vergit = vergit:main',
        ],
    },
)
