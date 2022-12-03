import os
import sys
import re
import subprocess
import shlex

try:
    from setuptools import setup, find_packages
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup, find_packages
    from distutils.command.install import install


VERSION = '0.6.4'


setup(
    name='websocket_server',
    version=VERSION,
    packages=find_packages("."),
    url='https://github.com/lakshaya-wq/python-ws-server',
    license='MIT',
    author='Lakshaya Utreja',
    author_email='lakshayautreja@gmail.com',
    install_requires=[],
    description='A simple fully working websocket-server in Python with no external dependencies',
    platforms='any',
    python_requires=">=3.6"
)
