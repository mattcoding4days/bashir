"""
When packaging LTF software, as libraries, or applications
this is the setup.py template that should be used
"""
import os
import subprocess

from setuptools import setup

# constants that should be front and center
VERSION = '0.1.0'
LICENSE = 'GPL3'
PKG_NAME = 'bashir'
REPO_URL = 'https://github.com/mattcoding4days/bashir'
EMAIL = 'mattltf@pm.me'

# dependency files
PRODUCTION: str = 'requirements/production.txt'
DEVELOPMENT: str = 'requirements/development.txt'

with open('README.md', 'r') as fh:
    long_description = fh.read()

# Get the current branch so we know which dependency file to load
command: str = 'git symbolic-ref HEAD'
try:
    result = subprocess.run(command,
                            shell=True,
                            check=True,
                            capture_output=True)
    branch: str = os.path.basename(result.stdout.decode('utf-8').strip('\n'))
except subprocess.CalledProcessError:
    # Hardcode to master for pipeline, for now
    branch: str = 'main'

if branch in 'master' or branch in 'main':
    with open(PRODUCTION, 'r') as depends:
        requirements = depends.read().splitlines()
else:
    with open(DEVELOPMENT, 'r') as depends:
        requirements = depends.read().splitlines()

setup(name=PKG_NAME,
      version=VERSION,
      install_requires=requirements,
      author="The Longtail Financial Devs",
      author_email=EMAIL,
      description="A scraper library for the needs of longtail financial",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url=REPO_URL,
      license=LICENSE,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.8',
          'Topic :: Internet',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities',
      ])
