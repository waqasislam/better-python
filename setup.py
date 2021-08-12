#!/usr/bin/env python3

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='better-python',
      version='1.0.o',
      description='Adding for functionality to python.',
      author='Waqas Islam',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['betterpython'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['forbiddenfruit'],
      python_requires='>=3.6',
      include_package_data=True)