#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'StatsApp',
    version = '0.1',
    description='StatsApp',
    url = 'https://github.com/llaaperi/StatsApp.git',
    author = 'Lauri Lääperi',
    author_email = 'lauri.laaperi@gmail.com',
    license = '',
    packages = find_packages(),
    package_data={'': []},
    include_package_data = True,
    install_requires = [
        'pandas==1.2.3',
        'matplotlib==3.3.4'
    ],
    entry_points={
        'console_scripts': [
            'statsapp=statsapp.__main__:main'
        ]
    }
)
