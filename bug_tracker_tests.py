import unittest
from bug_tracker import Project, Member, Bug

class BugTrackerTest(unittest.TestCase):

    def create_project_test(self):
        project = Project("P1","Project 1")
        project.add_member(Member("Joe","joe@example.com"))
        self.assertEqual(["Joe"], project.get_members())

    def create_bug_test(self):
        bug = Bug(1, "Bug number 1")
        self.assertEqual("new",bug.status)
        bug.add_comment("comment 1")
        bug.set_status("assigned")
        self.assertEqual("assigned",bug.status)
        self.assertEqual([],bug.comments)

