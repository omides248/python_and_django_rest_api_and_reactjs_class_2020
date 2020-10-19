username_in_database = [
    {
        "username": "omid",
        "password": "123"
    },
    {
        "username": "amin",
        "password": "123456"
    },
    {
        "username": "parvin",
        "password": "98765"
    },
    {
        "username": "nikkhah",
        "password": "56789"
    }
]


def is_authentication(username: str = None, password: str = None) -> bool:
    if username is None or password is None:
        return False
    else:
        for user in username_in_database:
            if username == user.get("username") and password == user.get("password"):
                return True
        return False


a = is_authentication("parvin", "98765")
print(a)
"".split()

print("new changed")
