class User:

    def __init__(self):
        self.first_name = "ali"

    def hasn(self):
        print("hasan")

    @classmethod
    def hasn2(cls):
        print("hasn2")


class User2:

    role = "old_role"

    def __init__(self):
        self.last_name = "aliee"


class Manager(User, User2):

    # def __init__(self):
    #     User.__init__(self)
    #     User2.__init__(self)
    #     print(self.first_name)
    #     print(self.last_name)
    @classmethod
    def hasn2(cls):
        print(cls.role)



Manager.hasn2()


