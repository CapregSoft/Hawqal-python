"""Python setup.py for hawqal package"""
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="hawqal",
    version="0.1.0",
    author="Husnain Khurshid",
    author_email="muhammadhusnainkh@gmail.com",
    description=(
        "Python package that contains the data of world's countries,states and their cities name"),
    license="BSD",
    keywords="atlas documentation tutorial",
    url="https://github.com/CapregSoft/Hawqal-python.git",
    packages=['hawqal'],
    long_description=read('README.md'),
)
