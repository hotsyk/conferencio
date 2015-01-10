#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import conferencio
version = conferencio.__version__

setup(
    name='conferencio',
    version=version,
    author='',
    author_email='gotsyk@gmail.com',
    packages=[
        'conferencio',
    ],
    include_package_data=True,
    install_requires=[
        'Django==1.7.2',
    ],
    zip_safe=False,
    scripts=['conferencio/manage.py'],
)
