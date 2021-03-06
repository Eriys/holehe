# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='',
    version="1.57",
    packages=find_packages(),
    author="megadose",
    install_requires=["termcolor","tqdm","lxml","bs4","httpx","trio"],
    description=" allows you to check if the mail is used on different sites like twitter, instagram , snapchat and will retrieve information on sites with the forgotten password function.",
    include_package_data=True,
    url='http://github.com/megadose/',
    entry_points = {'console_scripts': [' = core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
