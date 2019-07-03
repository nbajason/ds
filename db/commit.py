#!/usr/bin/env python

class Commit:
    def __init__(self):
        self.commands = []

    def add(self, command, *args):
        self.commands.append((command, args))

    def rollback(self):
        while len(self.commands)>0:
            cmd = self.commands.pop()

        # for cmd in self.commands[::-1]:
            # run command like set/unset
            # cmd[0] = set/unset
            # cmd[1] = args
            cmd[0](*cmd[1])
