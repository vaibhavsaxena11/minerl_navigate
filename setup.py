import os
from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="minerl_navigate",
    description="minerl-navigate - MineRL Navigate Video Dataset",
    long_description=readme,
    long_description_content_type="text/markdown",
    version="1.0.0",
    author="Vaibhav Saxena",
    author_email="saxena.vaibhav96@gmail.com",
    url="https://github.com/vaibhavsaxena11/minerl_navigate",
    packages=["minerl_navigate"],
    python_requires=">=3.7.*",
    install_requires=["numpy", "tensorflow>=2.4.1", "tensorflow-datasets>=4.2.0"],
    license="Attribution-NonCommercial-ShareAlike 4.0 International",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
    ],
)
