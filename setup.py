from setuptools import setup
from setuptools.command.build_py import build_py
from subprocess import call


class PasteurizeBuildCommand(build_py):
    def run(self):
        call(["pip", "install", "future"])
        call(["pasteurize", "./pyramda"])
        build_py.run(self)


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
    install_requires=['future'],
    tests_require=['nose', 'coverage', 'mock'],
    cmdclass={
        'build_py': PasteurizeBuildCommand
    },
    zip_safe=False
)
