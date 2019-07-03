#!/usr/bin/env python
from distutils.core import Command, setup

class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test import test_db
        test_db.test()

class ShellCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from db import db
        db.shell()

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
