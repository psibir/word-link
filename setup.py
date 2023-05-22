from setuptools import setup

setup(
    name='wordlink',
    version='1.0.0',
    author='Trevor Bloomfield',
    author_email='bloomfieldtm@gmail.com',
    packages=['wordlink'],
    install_requires=[
        'fuzzysearch',
        'prettytable'
    ],
    entry_points={
        'console_scripts': [
            'wordlink=wordlink:main'
        ]
    },
)
