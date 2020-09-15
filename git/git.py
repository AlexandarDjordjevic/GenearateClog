import subprocess
import json

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

    def getCommits(self, lastTag):
        process = subprocess.Popen(['git', 'log', '--pretty=tformat:"{\"Sha\":\"%h\", \"Message\":\"%B\"}"', '{}..HEAD'.format(lastTag)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.directory)
        out, err = process.communicate()
        commits = []
        output = out.decode('utf-8').replace('\n','\\n').replace('}"\\n"{', '}, {').replace('"{','[{').replace('}"','}]')[:-2]
        print(output)
        if output:
            jsonCommits = json.loads(output)
            for commit in jsonCommits:
                commits.append(commit)    
            return commits
        else:
            return ""

    def getLastTag(self):
        process = subprocess.Popen(['git',  'show-ref', '--tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.directory)
        out, err = process.communicate()
        tag = out.decode('utf-8').split('\n')[:-1][-1].split('/')[-1]
        return tag
        
        