#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Robin 'r0w' Weiland"
__date__ = "2020-03-04"
__version__ = "0.0.0"

__all__ = ()

from pathlib import Path
from setuptools import setup, find_packages

if __name__ == '__main__':
    with Path('README.md').open('r') as file: long_description = file.read()
    with Path('requirements.txt').open('r') as file:
        requirements = file.read().splitlines()

    setup(
        name='trayapp',
        packages=find_packages(),
        version='0.1.2',
        license='MIT',
        description="Library for creating system tray applications, based on Moses Palmér's 'pystray' library",
        long_description=long_description,
        long_description_content_type='text/markdown',
        author=__author__,
        author_email='robin.weiland@gmx.de',
        url='https://github.com/RoW171/trayPy',
        keywords=['systemtray', 'tray', 'app'],
        requires=requirements,
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.8',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.8',  # due to the walrus :=
    )
