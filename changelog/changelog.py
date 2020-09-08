import sys
import os
from git import *
from datetime import date


class Changelog:
    def __init__(self, version, repoUrl):
        self.version = version
        self.added = []
        self.changed = []
        self.fixed = []
        self.removed = []
        self.repoUrl = repoUrl
        
    def parse(self, commits):
        for commit in commits:
            for message in commit['Message'].split('\n'):           
                if '[ADD]' in message:
                    message = message.split(
                        '[ADD]')[1].strip()
                    self.added.append({'message':message, 'sha':commit['Sha']})
                if '[CHANGE]' in message:
                    message = message.split(
                        '[CHANGE]')[1].strip()
                    self.changed.append({'message':message, 'sha':commit['Sha']})
                if '[FIX]' in message:
                    message = message.split(
                        '[FIX]')[1].strip()
                    self.fixed.append({'message':message, 'sha':commit['Sha']})
                if '[REMOVE]' in message:
                    message = message.split(
                        '[REMOVE]')[1].strip()
                    self.removed.append({'message':message, 'sha':commit['Sha']})

    def __str__(self):
        result = "## " + '[{}]({}/releases/tag/{})'.format(self.version, self.repoUrl[:-4], self.version) + \
            " ({})".format(date.today()) + '\n'
        result = result + "\n### Added:\n\n"
        for commit in self.added:
            result = result + '- ' + commit['message'] + \
                ' ([{}]({}))'.format(commit['sha'], self.repoUrl[:-4] + '/commit/' + commit['sha']) + '\n'
        result = result + "\n### Changed:\n\n"
        for commit in self.changed:
            result = result + '- ' + commit['message'] + \
                ' ([{}]({}))'.format(commit['sha'], self.repoUrl[:-4] + '/commit/' + commit['sha']) + '\n'
        result = result + "\n### Fixed:\n\n"
        for commit in self.fixed:
            result = result + '- ' + commit['message'] + \
                ' ([{}]({}))'.format(commit['sha'], self.repoUrl[:-4] + '/commit/' + commit['sha']) + '\n'
        result = result + "\n### Removed:\n\n"
        for commit in self.removed:
            result = result + '- ' + commit['message'] + \
                ' ([{}]({}))'.format(commit['sha'], self.repoUrl[:-4] + '/commit/' + commit['sha']) + '\n'
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