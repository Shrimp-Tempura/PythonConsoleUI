from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='PyConsoleUI',
    version='1.0.0',
    author='Shrimp-Tempura', 
    author_email='lucas.cs.programming@gmail.com',
    packages=find_packages(),
    long_description=open('README.md').read()
)