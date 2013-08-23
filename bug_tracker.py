bug_ids = []
class Project(object):
    members = []
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def add_member(self, member):
        self.members.append((member.name, member.email))

    def get_members(self):
        return self.members

class Member(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Bug(object):
    comments = []
    def __init__(self, id, description, status="new", comment=""):
        if id in bug_ids:
            raise DuplicateIdException(id)
        else:
            self.id = id
            self.description = description
            self.status = status
            if comment != "":
                self.comments.append(comment)
                self.bug_ids.append(self.id)

    def set_status(self, status):
        self.status = status

    def add_comment(self, comment):
        self.comments.append(comment)

class DuplicateIdException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


