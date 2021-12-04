#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This module sets up the package for the lib_installer"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(    
    name="lib_installer",
    author="Justin Furuness",
    author_email="jfuruness@gmail.com",
    maintainer="Justin Furuness",
    maintainer_email="jfuruness@gmail.com",
    version="0.0.0",
    url="https://github.com/jfuruness/lib_installer.git",
    download_url='https://github.com/jfuruness/lib_installer.git',
    keywords=['Furuness', 'install', "Install"],
    license="BSD",
    description="Installs a new machine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'lib_installer = lib_installer.__main__:main',
        ]},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
