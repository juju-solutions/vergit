#!/usr/bin/env python
#
# Copyright 2012 Canonical Ltd.  This software is licensed under the
# GNU General Public License version 3 (see the file LICENSE).

from setuptools import setup


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
    description=('Tool for getting version from git'),
    long_description='Tool for getting version from git',
    license='GPL v3',
    url='https://github.com/johnsca/git-version',
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
