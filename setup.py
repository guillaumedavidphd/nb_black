#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from setuptools import setup


def readme(file_name):
    if os.path.isfile(file_name):
        with open(file_name, "r") as f:
            return f.read()


setup(
    name="nb_black",
    version="1.0.8.a",
    description="A simple extension for Jupyter Notebook and Jupyter Lab to beautify Python code automatically using Black.",
    long_description=readme(file_name="README.md"),
    long_description_content_type="text/markdown",
    keywords="black-formatter black-beautifier black jupyterlab-extension jupyter-notebook-extension",
    url="https://github.com/guillaumedavidphd/nb_black",
    author="Khoa Duong",
    author_email="dnanhkhoa@live.com",
    license="MIT",
    py_modules=["nb_black", "lab_black"],
    zip_safe=False,
    install_requires=[
        "black >= 19.3; python_version >= '3.6'",
        "ipython",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
