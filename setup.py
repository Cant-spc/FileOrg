from setuptools import setup, find_packages

setup(
    name="filefix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'typer>=0.4.1',
    ],
    entry_points={
        'console_scripts': [
            'filefix=filefix.core:app',
        ],
    },
)
