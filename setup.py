#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
import os
import re

from setuptools import find_packages, setup


current_dir = os.path.dirname(os.path.realpath(__file__))
with open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()


def get_meta():
    meta_re = re.compile(r"(?P<name>__\w+__) = '(?P<value>[^']+)'")
    meta_d = {}
    with open(os.path.join(current_dir, 'aiobearychat/__init__.py'),
              encoding='utf8') as fp:
        for match in meta_re.finditer(fp.read()):
            meta_d[match.group('name')] = match.group('value')
    return meta_d


requirements = [
    'attrs',
]

extras_require = {
    '': requirements,
    'aiohttp': 'aiohttp',
}

meta_d = get_meta()
setup(
    name='aiobearychat',
    version=meta_d['__version__'],
    description='An async bearychat API library for Python',
    long_description=readme,
    author='mozillazg',
    author_email='mozillazg101@gmail.com',
    url='https://github.com/mozillazg/aiobearychat',
    packages=find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']
    ),
    package_dir={'aiobearychat':
                 'aiobearychat'},
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    license='MIT',
    zip_safe=False,
    # entry_points={
    #     'console_scripts': [
    #         'aiobearychat = aiobearychat.__main__:main',
    #     ],
    # },
    keywords='aiobearychat',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
