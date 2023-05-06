'''
name: 
    The name of the package. We can give our package any name of our choice.
version: 
    The starting version should be 0.1 because, with any update, it automatically increases it to one decimal place.
description:
    description of our package and its functionalities and uses.
long_description: 
    explanatory description of our package
author: 
    We can specify the creator of the package here
packages: 
    Here we give the name by which we want our package to be called or imported
install_requires: 
    If our package has a prerequisite package


python3 setup_filename.py sdist bdist_wheel
pip3 install package_name 

'''
from setuptools import setup
setup(name="packageharry",
version="0.3",
description="This is code with harry package",
long_description = "This is a very very long description",
author="Harry",
packages=['packageharry'],
install_requires=[])
