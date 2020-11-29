from src.enums import EnumRole
from src.models.user import User
from src.views.login_logout_view import LoginLogoutView


class Session:
    __sessions = {
        "omides248": {
            "role": EnumRole.ADMIN
        }
    }

    @classmethod
    def save(cls, username: str = None, role: str = None) -> bool:
        if User.exists_with_username(username):
            if not cls.exists_with_username(username):
                cls.__sessions[username] = dict(role=role)
                return True
        return False

    @classmethod
    def get_first_session(cls) -> dict:
        return list(cls.__sessions.values())[0] if cls.__sessions else {}

    @classmethod
    def exists_with_username(cls, username: str = None) -> bool:
        return True if cls.__sessions.get(username) else False

    @classmethod
    def is_admin(cls) -> bool:
        return True if cls.get_first_session().get("role") == EnumRole.ADMIN else False

    @classmethod
    def is_employee(cls) -> bool:
        return True if cls.get_first_session().get("role") == EnumRole.EMPLOYEE else False

    @classmethod
    def is_customer(cls) -> bool:
        return True if cls.get_first_session().get("role") == EnumRole.CUSTOMER else False

    @classmethod
    def get_all_session(cls):
        return cls.__sessions


LoginLogoutView.login()
Session.get_first_session()
