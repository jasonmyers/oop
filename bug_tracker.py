class Project(object):

    def __init__(self, name, description):
        pass

    def add_member(self, member):
        pass

    def get_members(self):
        return ["Joe"]

class Member(object):

    def __init__(self, name, email):
        pass

class Bug(object):
    bug_ids = []
    comments = []
    def __init__(self, id, description, status="new", comment=""):
        self.id = id
        self.description = description
        self.status = status
        if comment != "":
            self.comments.append(comment)
        self.bug_ids.append(self.id)

    def set_status(self, status):
        self.status = status

    def add_comment(self, comment):
        pass

