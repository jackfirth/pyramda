from setuptools import setup
from subprocess import call

setup(
    name='pyramda',
    version='0.1',
    description='A Python package for curried functional programming',
    url='http://github.com/jackfirth/pyramda',
    author='Jack Firth',
    author_email='jackhfirth@gmail.com',
    packages=[
        'pyramda',
        'pyramda.dictionary',
        'pyramda.function',
        'pyramda.iterable',
        'pyramda.logic',
        'pyramda.math',
        'pyramda.private',
        'pyramda.private.curry_spec',
        'pyramda.relation'
    ],
    tests_require=['nose', 'coverage', 'mock'],
    zip_safe=False
)
