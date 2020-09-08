import sys
import os
from git import *
from datetime import date


class Changelog:
    def __init__(self, version):
        self.version = version
        self.added = []
        self.changed = []
        self.fixed = []
        self.removed = []
        self.url = ''
        
    def parse(self, commits):
        for commit in commits:
            if '[ADD]' in commit.message:
                commit.message = commit.message.split(
                    '[ADD]')[1].strip().split('\n')[0]
                self.added.append(commit)
            if '[CHANGE]' in commit.message:
                commit.message = commit.message.split(
                    '[CHANGE]')[1].strip().split('\n')[0]
                self.changed.append(commit)
            if '[FIX]' in commit.message:
                commit.message = commit.message.split(
                    '[FIX]')[1].strip().split('\n')[0]
                self.fixed.append(commit)
            if '[REMOVE]' in commit.message:
                commit.message = commit.message.split(
                    '[REMOVE]')[1].strip().split('\n')[0]
                self.removed.append(commit)

    def __str__(self):
        result = "## " + self.version + \
            " ({})".format(date.today()) + '\n'
        result = result + "\n### Added:\n\n"
        for commit in self.added:
            result = result + '- ' + commit.message + \
                ' ([{}]({}))'.format(commit.sha, commit.url) + '\n'
        result = result + "\n### Changed:\n\n"
        for commit in self.changed:
            result = result + '- ' + commit.message + \
                ' ([{}]({}))'.format(commit.sha, commit.url) + '\n'
        result = result + "\n### Fixed:\n\n"
        for commit in self.fixed:
            result = result + '- ' + commit.message + \
                ' ([{}]({}))'.format(commit.sha, commit.url) + '\n'
        result = result + "\n### Removed:\n\n"
        for commit in self.removed:
            result = result + '- ' + commit.message + \
                ' ([{}]({}))'.format(commit.sha, commit.url) + '\n'
        result = result + "\n---\n"
        return result

    def saveToFile(self):
        #append file!
        with open('CHANGELOG.md', 'r+') as file:
            firstLine = file.readline()
            file.seek(len(firstLine), 0)
            content = file.read()
            file.seek(0, 0)
            file.write("# Changelog \n\n")
            file.write(str(self))
            file.write(content)