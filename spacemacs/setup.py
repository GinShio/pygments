#!/usr/bin/python3
from setuptools import setup, find_packages

setup(
    name='pygments-style-spacemacs',
    version='1.0.0',
    description='Pygments version of the spacemacs theme, Based on nashamri/spacemacs-theme.',
    keywords=['pygments', 'style', 'spacemacs'],
    author='Xin \'GinShio\' Liu',
    author_email='ginshio78@gmail.com',
    url='https://github.com/ginshio/pygments/tree/master/spacemacs/pygments_style_spacemacs',
    license='GPLv3',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    zip_safe=False,
    entry_points="""[pygments.styles]
        spacemacs-light=pygments_style_spacemacs.spacemacs_light:SpacemacsLightStyle
        spacemacs-dark=pygments_style_spacemacs.spacemacs_dark:SpacemacsDarkStyle""",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
