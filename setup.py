from setuptools import setup, find_packages

setup(
    name='card_game',
    description='Card Game',
    long_description='A simple card game.',
    packages=find_packages(exclude=["*tests*"]),
    package_data={'': ['*.yaml']},
    version='1.0.0',
    install_requires=[
    ],
    extras_require={
        'dev': [
            'pycodestyle==2.9.*',
            'flake8==5.0.*',
        ],
    }
)
