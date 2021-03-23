import os
from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='minerl_navigate',
    description='minerl-navigate - MineRL Navigate Video Dataset',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='1.1.0',
    author='Vaibhav Saxena',
    author_email='saxena.vaibhav96@gmail.com',
    url='https://github.com/vaibhavsaxena11/minerl_navigate',
    packages=['minerl_navigate'],
    install_requires=['numpy', 'tensorflow', 'tensorflow-datasets'],
    license='Attribution-NonCommercial-ShareAlike 4.0 International',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
