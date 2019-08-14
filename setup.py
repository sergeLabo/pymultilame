#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pymultilame',
    version='1.57',
    plateformes = 'LINUX',
    packages=find_packages(),
    packages_dir = {'' : 'pymultilame'},
    author='sergeLabo',
    description='Python Labomedia Utilities',
    url='https://labomedia.org',
    download_url='https://github.com/sergeLabo/pymultilame',
    license='GPL Version 3',
    keywords = ["blender", "network", "tools"],
    classifiers = [ "Programming Language :: Python :: 3",
                    "Development Status :: 4 - Beta",
                    "Intended Audience :: Developers",
                    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                    "Operating System :: Debian",
                    "Topic :: Blender Game Engine",
                    "Topic :: Network",
                    "Topic :: System"],
    long_description=open('README.md').read()
    )
