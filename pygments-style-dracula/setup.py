#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='pygments-style-dracula',
    version='1.2.5.1',
    description='Pygments version of the dracula theme, based on dracula/pygments.',
    keywords=['pygments', 'style', 'dracula'],
    author='Rob G, Chris Bracco, Zeno Rocha',
    author_email='wowmotty@gmail.com, chris@cbracco.me, hi@zenorocha.com',
    maintainer='GinShio',
    maintainer_email='ginshio78@gmail.com',
    url='https://draculatheme.com/pygments',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    zip_safe=False,
    entry_points="""[pygments.styles]
        dracula=pygments_style_dracula.dracula:DraculaStyle""",
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
