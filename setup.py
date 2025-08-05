from setuptools import setup, find_packages

setup(
    name="filefix",
    author="Tanish Gupta",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        'typer>=0.4.1',
    ],
    entry_points={
        'console_scripts': [
            'filefix=filefix.core:app',
        ],
    },
    description="A CLI tool to organize files in a directory.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tanishgupta/filefix",
)
