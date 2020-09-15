import sys
from changelog.changelog import Changelog
from git.git import Git

usage = '''
Usage:
    clgenerator <repo path> <release version>'''

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(usage)
        sys.exit()
    repo = Git(sys.argv[1])
    latestTag = repo.getLastTag()
    commits = repo.getCommits(latestTag)
    changelog = Changelog(sys.argv[2], repo.getURL())
    changelog.parse(commits)
    changelog.saveToFile(sys.argv[1])
    

