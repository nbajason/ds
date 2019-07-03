#!/usr/bin/env python

import sys
import datetime
from db.datastore import DataStore

import pdb

class DB:
    _commands_ = {
                'set':0,
                'get':1,
                'unset':2,
                'numequalto':3,
                'begin':4,
                'rollback':5,
                'commit':6,
                'end':7,
                'exit':8,
                }

    def __init__(self):
        self._datastore_ = DataStore()

    def run(self, query):
        # pdb.set_trace()
        tokens = query.split(' ')
        command, args = tokens[0].lower(), (self._parse_token_(token) for token in tokens[1:])

        # swith - case
        if command in DB._commands_:
            try:
                func = getattr(self, command, lambda: "command of {} is invalid, please try {}".format(command, self._commands_))
                return func(*args)
            except Exception as e:
                print('error occurs when try to run command:', e)
        else:
            print("command of {} is invalid, please try command in {}".format(command, self._commands_.keys()))

    def _parse_token_(self, token):
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return token

    def set(self, key, value):
        """
        SET [key name] [value]
        no space
        """
        self._datastore_.set(key, value)
        return

    def get(self, key):
        return self._datastore_.get(key) if self._datastore_.has_key(key) else 'NULL'

    def unset(self, key):
        self._datastore_.unset(key)
        return

    def numequalto(self, value):
        return self._datastore_.numequalto(value)

    def begin(self):
        self._datastore_.begin()

    def rollback(self):
        if self._datastore_.no_commits():
            return "INVALID ROLLBACK: NO COMMITS BEFORE"
        else:
            self._datastore_.rollback()

    def commit(self):
        self._datastore_.commit()

    def end(self):
        sys.exit()

    def exit(self):
        sys.exit()

def shell():
    db = DB()
    print("DB 1.0 in memory ({})".format(datetime.datetime.now()))
    print("Commands: {}".format([c for c in db._commands_.keys()]))
    print("-----------------------------------------------------------")

    while True:
        sys.stdout.write('>>> ')
        sys.stdout.flush()
        query = sys.stdin.readline().strip()
        if query != None:
            result = db.run(query)
            if result != None:
                print(result)

if __name__ == '__main__':
    shell()
