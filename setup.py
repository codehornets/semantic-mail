from setuptools import setup, find_packages

setup(
    name="semantic-mail",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'smail=src.cli:cli',
        ],
    },
) 