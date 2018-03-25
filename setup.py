# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='asymmetric tsp',
    version='0.1.0',
    description='Solver for Asymmetric Traveling Salesman Problem',
    long_description=readme,
    author='Naohiro Heya',
    url='https://github.com/SyureNyanko/asymmetric_tsp',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

