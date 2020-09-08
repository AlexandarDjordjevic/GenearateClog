from changelog.changelog import Changelog
from git.git import Git

if __name__ == '__main__':
    repo = Git('/home/alexandar/TestRepo')
    commits = repo.getCommits()
    changelog = Changelog("v1.0.2")
    changelog.parse(commits)
    changelog.saveToFile()
