import subprocess


class Git:
    def __init__(self, directory):
        self.directory = directory
        self.url = self.getURL()
        
    def getURL(self):
        process = subprocess.Popen(
            ["git", "remote", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.directory)
        out, err = process.communicate()
        remotes = out.decode('utf-8').split('\n')[:-1]
        for remote in remotes:
            url, tpe = remote.split('\t')[1].split(' ')
            if tpe == '(fetch)':
                if "@" in url:
                    # git@github.com:AlexandarDjordjevic/TestRepo
                    # https://github.com/AlexandarDjordjevic/TestRepo.git
                    server, repo = url.split('@')[1].split(':')
                    url = 'https://' + server + '/' + repo
            return url

    def getCommits(self):
        process = subprocess.Popen(['git', 'log', '--pretty=tformat:"%h %B"'],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.directory)
        out, err = process.communicate()
        commits = []
        for row in out.decode('utf-8').split('\n'):
            if row:
                if row[0] == '"':
                    commits.append(Commit(row[1:7], row[8:], self.url))
                else:
                    commits.append(
                        Commit(commits[-1].sha, row, self.url))
        return commits

class Commit:
    def __init__(self, sha, message, url):
        self.sha = sha
        self.url = url[:-4] + '/commit/' + self.sha
        self.message = message
