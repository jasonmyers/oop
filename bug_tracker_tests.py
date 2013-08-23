import unittest
from bug_tracker import Project, Member

class BugTrackerTest(unittest.TestCase):

    def create_project_test(self):
        project = Project("P1","Project 1")
        project.add_member(Member("Joe","joe@example.com"))
        self.assertEqual(["Joe"], project.get_members())