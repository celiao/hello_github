# See http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'hello_github',
    version = '0.1',
    author = 'Celia Oakley',
    author_email = 'celia.oakley@alumni.stanford.edu',
    description = 'A test package',
    keywords = ['testing', 'hello', 'example'],
    url = 'https://github.com/celiao/hello_github',   # URL to github repo
    download_url = 'https://github.com/celiao/hello_github/tarball/0.1',
    packages = ['hello_github'],
    long_description=read('README.rst'),
    install_requires = ['requests>=0.11.1'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
