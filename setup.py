#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='pymultilame',
    packages = ["pymultilame"],
    version='0.03',
    description='Python Labomedia Utilities',
    author='sergeLabo',
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
    long_description = """\
        Tools used every day
        --------------------
        Tools used in Blender Game Engine and Python Script
        """,

    py_modules=['http_download',
                'OSC3',
                'tcpclient',
                'tcptwisted',
                'mytools']
     )

# #'./blender/blendersound',
                # #'./blender/blendertempo',
                # #'./blender/blendertexture',
                # #'./blender/blendertools',
                # #'./blender/blenderviewport',
