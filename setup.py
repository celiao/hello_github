# http://pythonhosted.org/an_example_pypi_project/setuptools.html

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#with open('README.rst') as file:
#    long_description = file.read()
#

#def read(fname):
#    with open(fname) as fp:
#        content = fp.read()
#    return content

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
    #long_description=long_description,
    long_description=read('README.rst'),
    #long_description=(read("README.rst")),
    install_requires = ['requests>=0.11.1'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
