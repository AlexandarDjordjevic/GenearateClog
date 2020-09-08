#/bin/python3.6
import unittest
from changelog.changelog import Changelog
from git.git import Commit


class TestChangelog(unittest.TestCase):

    def test_parse_version(self):
        commits = []
        commits.append(
            Commit("1234567", "[ADD] Commit 1", "https://example.com/test.git"))
        
        changelog = Changelog("v1.0.0")
        changelog.parse(commits)
        self.assertEqual(changelog.version, "v1.0.0")
 
    def test_parse_message(self):
        commits = []
        commits.append(
            Commit("1234567", "[ADD] Commit 1", "https://example.com/test.git"))
        
        changelog = Changelog("v1.0.0")
        changelog.parse(commits)     
        self.assertEqual(changelog.added[0].message, "Commit 1")
        
    def test_parse_message_multiple_lines(self):
        commits = []
        commits.append(
            Commit("1234567", '"[ADD] Commit 1\n[REMOVE] Remove 1', "https://example.com/test.git"))
        
        changelog = Changelog("v1.0.0")
        changelog.parse(commits)     
        self.assertEqual(changelog.added[0].message, "Commit 1")
        self.assertEqual(changelog.removed[0].message, "Remove 1")
               
    def test_parse_sha(self):
        commits = []
        commits.append(
            Commit("1234567", "[ADD] Commit 1", "https://example.com/test.git"))
        
        changelog = Changelog("v1.0.0")
        changelog.parse(commits)     
        self.assertEqual(changelog.added[0].sha, "1234567")


if __name__ == '__main__':
    unittest.main()
