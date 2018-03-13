#!/usr/bin/env python

from setuptools import setup

setup_info = dict(
      name='protoslib',
      version='0.1',
      description='Python library for interacting with the internal Protos API',
      author='Alex Giurgiu',
      author_email='alex@giurgiu.io',
      url='https://github.com/nustiueudinastea/protoslib-py',
      packages=['protoslib'],
     )

setup(**setup_info)