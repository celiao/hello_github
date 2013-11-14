from setuptools import setup
setup(
    name = 'hello_github',
    packages = ['hello_github'],
    version = '0.1',
    install_requires = ['requests>=0.11.1'],
    description = 'A test file',
    author = 'Celia Oakley',
    author_email = 'celia.oakley@alumni.stanford.edu',
    url = 'https://github.com/celiao/hello_github',   # URL to github repo
    download_url = 'https://github.com/celiao/hello_github/tarball/0.1',
    keywords = ['testing', 'hello', 'example'],
    classifiers = [],
)
