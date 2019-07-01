#!/usr/bin/env python
from distutils.core import Command, setup

class TestCommand(Command):
    user_options = []

    def initialize_options:
        pass

setup(
    name = 'db',
    version = '1.0',
    description = 'test db',
    packages = ['db',],
    long_description=open('README.md').read(),
    cmdclass = {
        'shell': ShellCommand,
        'test': TestCommand,
    },
)
