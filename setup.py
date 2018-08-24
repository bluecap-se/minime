#!/usr/bin/python
# -*- coding: utf-8 -*-

import minime

from setuptools import setup


with open('README.md') as f:
    readme = f.read()
with open('HISTORY.md') as f:
    history = f.read()

setup(
    name=minime.__title__,
    description='MiniMe - An online URL shortener',
    long_description=readme,
    version=minime.__version__,
    author='bluecap-se',
    author_email='hello@bluecap.se',
    url='https://github.com/bluecap-se/minime',
    license='MIT',
    zip_safe=False,
    platforms='any',
    packages=['minime'],
    install_requires=requirements,
    keywords=['mini', 'minime', 'url', 'short', 'tiny'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ]
)
