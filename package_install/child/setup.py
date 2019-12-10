import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'COPYRIGHT.txt')) as copy_right:
    COPYRIGHT = copy_right.read()

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='travis',
    version='0.1.0',
    scripts=['script'],
    packages=[f'travis.{x}' for x in find_packages('travis')],
    license=COPYRIGHT,
    description='Packaging testing.',
    long_description=README,
    url='https://www.almeki.io/',
    author='Yannick KIKI',
    author_email='seyive.kiki@gmail.com',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
