"""Python setup.py for hawqal package"""
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hawqal",
    version="0.1.5.8",
    description="Python package that contains the data of world's countries,states and their cities name",
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    url="https://github.com/CapregSoft/Hawqal-python.git",
    keywords=['husnain khurshid', 'capregsoft',
              'hawqal', 'world data', 'states'],
    author="Husnain Khurshid",
    author_email="muhammadhusnainkh@gmail.com",
    packages=["hawqal", "dal", "database"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)
