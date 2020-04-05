

from setuptools import setup, find_packages

with open("README.md",'r') as f:
    long_description = f.read()

setup(
    name="nprpuzzle",
    version="0.1",
    packages=find_packages(),

    scripts=[],

    author="Evan Berkowitz, NPR Puzzle Fan",
    author_email="nprpuzzle@evanberkowitz.com",
    description="Scrape the NPR Puzzle page and build a podcast from it.",
    long_description=long_description,
    keywords="npr puzzle podcast",

    url="https://github.com/evanberkowitz/npr-sunday-puzzle-podcast",

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
