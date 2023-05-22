from setuptools import setup

setup(
    name='wordlink',
    version='1.0.0',
    author='Trevor Bloomfield',
    author_email='bloomfieldtm@gmail.com',
    description='Word Link Generator',
    py_modules=['wordlink'],
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
