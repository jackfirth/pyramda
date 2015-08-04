from setuptools import setup
from setuptools.command.install import install
from subprocess import call


class PastuerizeInstallCommand(install):
    def run(self):
        call(["pasteurize", "./pyramda"])
        install.run(self)


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
    tests_require=['nose', 'coverage'],
    cmdclass={
        'install': PastuerizeInstallCommand,
    },
    zip_safe=False
)
