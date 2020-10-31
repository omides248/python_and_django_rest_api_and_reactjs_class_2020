class User:

    def __init__(self):
        self.first_name = "ali"


class User2:

    def __init__(self):
        self.last_name = "aliee"


class Manager(User, User2):

    def __init__(self):
        User.__init__(self)
        User2.__init__(self)
        print(self.first_name)
        print(self.last_name)


