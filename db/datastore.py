#!/usr/bin/env python

from db.commit import Commit

class DataStore:
    def __init__(self):
        self.commits = []
        self.data = {}
        self.value_counts = {}

    def get(self, key):
        return self.data[key]

    def set(self, key, value, logging=True):
        has_key = self.has_key(key)

        # store command into commits after run 'begin'
        if len(self.commits)>0 and logging:
            commit = self.commits[-1]
            if has_key:
                commit.add(self.set, key, self.get(key), False)
            else:
                commit.add(self.unset, key, False)

        if has_key:
            old_value = self.get(key)
            if old_value != value:
                self._update_value_count_(old_value, -1)
        self._update_value_count_(value, 1)

        self.data[key] = value
        print('set {}: {}'.format(key, value))

    def unset(self, key, logging=True):
        if self.has_key(key):
            # after valid unset, store command into commits
            if len(self.commits)>0 and logging:
                self.commits[-1].add(self.set, key, self.get(key), False)

            self._update_value_count_(self.get(key), -1)
            del self.data[key]
            print('deleted:', key)
        else:
            print('no key: {}'.format(key))

    def _update_value_count_(self,value,count):
        if (value in self.value_counts):
            self.value_counts[value] += count
        else:
            self.value_counts[value] = count

        if self.value_counts[value] < 0:
            print('self.value_counts[value] < 0')
            self.value_counts[value] = 0

    def has_key(self, key):
        return (key in self.data)

    def commit(self):
        self.commits = []

    def no_commits(self):
        return len(self.commits) == 0

    def begin(self):
        self.commits.append(Commit())

    def rollback(self):
        # get the command from commit
        commit = self.commits.pop()
        # run command by commit.rollback()
        commit.rollback()

    def numequalto(self,value):
        if value not in self.value_counts:
            return 0
        else:
            return self.value_counts[value]
