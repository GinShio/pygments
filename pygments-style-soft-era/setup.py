#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='pygments-style-soft-era',
    version='1.0.3',
    description='Pygments version of the soft-era theme.',
    keywords=['pygments', 'style', 'soft-era'],
    author='Audrey Moon',
    maintainer='GinShio',
    maintainer_email='ginshio78@gmail.com',
    utl='http://soft-aesthetic.club/soft-era.html',
    download_url='https://github.com/GinShio/pygments',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    zip_safe=False,
    entry_points="""[pygments.styles]
        soft-era=pygments_style_soft_era.soft_era:SoftEraStyle""",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
