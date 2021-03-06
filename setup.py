# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name="todolist",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click",
        "enum34",
        "inject",
        "gxredis",
        "pytest",
    ],
    license="MIT",
    scripts=["bin/todo"],
)
