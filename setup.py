# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='GlobalVars',
    version='0.0.5',
    author='Matheus Menezes Almeida',
    author_email='mrotame@gmail.com',
    description=u'Using environment variable to store global vars to the enrite project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mrotame/GlobalVars',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)