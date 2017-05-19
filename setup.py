try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup

# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

config = {
    description: 'moduli di una semplice calcolatrice in python',
    author: 'Enrico Capone',
    url: 'https://github.com/enrico84/pyCalcolatrice',
    download_url: 'https://github.com/enrico84/pyCalcolatrice',
    author_email: 'enrico8484@gmail.com',
    version: '1.0',
    #packages: find_packages(),
    packages=find_packages(exclude=('tests', 'docs'))
    scripts: [],
    name: 'source'
}
