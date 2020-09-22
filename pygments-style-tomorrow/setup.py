#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='pygments-style-tomorrow',
    version='1.0.0',
    description='Pygments version of the tomorrow theme, Based on mozmorris/tomorrow-pygments.',
    keywords=['pygments', 'style', 'tomorrow'],
    author='Moz Morris',
    author_email='moz@earthview.co.uk',
    maintainer='GinShio',
    maintainer_email='ginshio78@gmail.com',
    url='https://github.com/mozmorris/tomorrow-pygments',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    zip_safe=False,
    entry_points="""[pygments.styles]
        tomorrow-day=pygments_style_tomorrow.tomorrow:TomorrowStyle
        tomorrow-night=pygments_style_tomorrow.tomorrownight:TomorrownightStyle
        tomorrow-night-blue=pygments_style_tomorrow.tomorrownightblue:TomorrownightblueStyle
        tomorrow-night-bright=pygments_style_tomorrow.tomorrownightbright:TomorrownightbrightStyle
        tomorrow-night-eighties=pygments_style_tomorrow.tomorrownighteighties:TomorrownighteightiesStyle""",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
