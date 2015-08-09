#!/usr/bin/env python

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
#from codecs import open
#from os import path

#here = path.abspath(path.dirname(__file__))

#with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
 #   long_description = f.read()

setup(
    name='graphistry',

    version='0.0.22',
    py_modules = ['graphistry.etl'],
    description = 'Visualize node-link graphs using Graphistry\'s cloud',
    #long_description=long_description,

    url='https://github.com/graphistry/pygraphistry',

    author='Graphistry',
    author_email='pygraphistry@graphistry.com',
    setup_requires=['numpy'],
    install_requires=['numpy', 'pandas', 'requests', 'future'],

    license='BSD',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',

        'Topic :: Scientific/Engineering :: Visualization',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='graph plot visualization pandas',

    packages=find_packages(exclude=['contrib', 'tests*'])
)
