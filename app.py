from changelog.changelog import Changelog
from git.git import Git

if __name__ == '__main__':
    repo = Git('/home/syrmia/Documents/Work/gitpy/TestRepo')
    changelog = Changelog(repo, "v1.0.0")
    changelog.prepare()
    changelog.saveToFile()
