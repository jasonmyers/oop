import unittest
from bug_tracker import Project, Member, Bug, DuplicateIdException

class BugTrackerTest(unittest.TestCase):

    def create_project_test(self):
        project = Project("P1","Project 1")
        self.assertEqual("P1",project.name)
        self.assertEqual("Project 1",project.description)

    def create_member_test(self):
        member = Member("Joe","joe@example.com")
        self.assertEqual("Joe",member.name)
        self.assertEqual("joe@example.com", member.email)

    def add_members_to_project_test(self):
        project = Project("P1","Project 1")
        # add one member
        project.add_member(Member("Joe","joe@example.com"))
        self.assertEqual([("Joe","joe@example.com")], project.get_members())
        #add second member
        project.add_member(Member("Jane","jane@example.com"))
        self.assertEqual([("Joe","joe@example.com"), ("Jane","jane@example.com")], project.get_members())

    def create_bug_test(self):
        bug = Bug(1, "Bug number 1")
        self.assertEqual("new",bug.status)
        # set status to assigned
        bug.set_status("assigned")
        self.assertEqual("assigned",bug.status)
        # add comment "comment 1"
        bug.add_comment("comment 1")
        self.assertEqual(["comment 1"],bug.comments)

    def create_duplicate_bug_id_test(self):
        bug = Bug(1, "Bug number 1")
        self.assertRaises(DuplicateIdException, bug.__init__(bug, 1, "Bug number 2"))

