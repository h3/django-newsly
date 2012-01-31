#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
django-newsly
"""

VERSION = __import__('newsly').VERSION

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
#   'simplejson',
]

#tests_require = [
   #'logbook',
   #'nose',
   #'unittest2',
#]

setup(
    name='newsly',
    version=VERSION,
    author='Maxime Haineault',
    author_email='max@motion-m.ca',
    url='https://github.com/h3/django-newsly',
    description = 'Simple drop-in news app for django',
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    license='BSD',
    install_requires=install_requires,
    dependency_links=[],
   #tests_require=tests_require,
   #extras_require={'test': tests_require},
   #test_suite='nose.collector',
    include_package_data=True,
#   entry_points = {
#       'console_scripts': [
#           'duke = bin.client:main',
#       ],
#   },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)




