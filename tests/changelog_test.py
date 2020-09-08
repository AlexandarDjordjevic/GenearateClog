import unittest
from changelog.changelog import Changelog
from git.git import Commit


class TestChangelogMethods(unittest.TestCase):

    def test_prepare(self):
        commits = []
        commits.append(
            Commit("1234567", "[ADD] Commit 1", "https://example.com/test.git"))
        changelog = Changelog(commits, "v1.0.0")
        changelog.prepare()
        self.assertEqual(changelog.version, "v1.0.0")
        # self.assertEqual(changelog.added)


if __name__ == '__main__':
    unittest.main()
