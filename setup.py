#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-checkipdb',
    version='1.0.5',
    author='Andreu Vallbona',
    author_email='avallbona@gmail.com',
    maintainer='Andreu Vallbona',
    maintainer_email='avallbona@gmail.com',
    license='MIT',
    url='https://github.com/avallbona/pytest-checkipdb',
    description='plugin to check if there are ipdb debugs left',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=[
        'pytest_checkipdb'
    ],
    install_requires=[
        'pytest>=2.9.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'checkipdb = pytest_checkipdb',
        ],
    },
)
