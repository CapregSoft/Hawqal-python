"""Python setup.py for hawqal package"""
from setuptools import find_packages, setup


setup(
    name="hawqal",
    version="0.1.0",
    description="Python package that contains the data of world's countries,states and their cities name",
    url="https://github.com/CapregSoft/Hawqal-python.git",
    long_description_content_type="text/markdown",
    author="capregsoft",
    packages=find_packages(exclude=["tests", ".github"]),
    entry_points={
        "console_scripts": ["hawqal = hawqal.__main__:main"]
    },
)
