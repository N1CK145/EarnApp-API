from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'UNOFFICIAL Python bindings for Earnapp dashboard API'
LONG_DESCRIPTION = 'A package that allows you to connect to Earnapp API and interact with your data.'

# Setting up
setup(
    name="pyEarnapp",
    version=VERSION,
    author="fazalfarhan01 (Mohamed Farhan Fazal)",
    author_email="<fazal@ffehost.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'earnapp', 'passive income', 'earnapp api',
              'earnapp dashboard', 'requests', "python earnapp"],
    classifiers=[
        "Development Status :: 1 - Release",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
