from itertools import count as itertools_count

from src.enums import EnumRole


class User:
    __table = [
        {
            "id": "1",
            'username': 'omides248',
            "first_name": "omid",
            "last_name": "esmaeili",
            "password": "1234",
            'role': EnumRole.ADMIN
        },
    ]
    __id = itertools_count(2)

    @classmethod
    def get_all_users(cls) -> list:
        return cls.__table

    @classmethod
    def get_user(cls, username: str = None) -> dict:
        for user in User.get_all_users():
            if user.get("username") == username:
                return user
        return {}

    @classmethod
    def save(cls, username: str = None, first_name: str = None, last_name: str = None, password: str = None,
             role: str = None) -> bool:

        cls.__table.append(
            dict(
                id=str(next(cls.__id)),
                uesrname=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                role=role
            )
        )
        return True

    @classmethod
    def exists_with_username(cls, username: str = None) -> bool:
        for user in User.get_all_users():
            if user.get("username") == username:
                return True
        return False


# User.save("hasan", "first1", "last2", "1234", "admin")
# print(User.get_all_users())
