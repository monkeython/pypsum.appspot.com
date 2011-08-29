from __future__ import with_statement
from setuptools import setup
import sys
import os

wd = os.path.dirname(os.path.abspath(__file__))
os.chdir(wd)
sys.path.insert(1, wd)

name = 'app'
pkg = __import__(name)
author, email = pkg.__author__.rsplit(' ', 1)

long_description = pkg.__doc__

python_version = sys.version_info[:2]
url = 'http://projects.monkeython.com/%s' % name

application = {
    'name': name,
    'version': pkg.__version__,
    'author': author,
    'author_email': email.strip('<>'),
    'url': '%s/html' % url,
    'description': "Pypsum application for Google Appengine",
    'long_description': long_description,
    'classifiers': pkg.__classifiers__,
    'py_modules': [name],
    #'setup_requires': ['setuptools', 'distribute'],
    'install_requires': ['setuptools', 'pypsum'],
    'package_data': {'': ['*.yaml']}}

if __name__ == '__main__':
    setup(**application)

