#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 13:35:30 2025

@author: nayandusoruth
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()


setup(
    name="GeneralUtilities",
    version="1.2",
    description="""A personal library of generally useful functions, methods and classes""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nayan Dusoruth",
    packages=find_packages(include=["GeneralUtilities"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    license="MIT",
    url="https://github.com/topHatSurgeon/GeneralUtilities",
)